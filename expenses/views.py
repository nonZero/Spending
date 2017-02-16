from django.contrib import messages
from django.http.response import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from expenses.forms import ExpenseForm, FeebackForm, CommentForm
from . import models


def list_months(request):
    qs = models.Expense.objects.dates('date', 'month').order_by('-date')
    return render(request, "expenses/expense_months.html", {
        'dates': qs,
    })


def list(request, year=None, month=None):
    qs = models.Expense.objects.all()
    if year:
        qs = qs.filter(date__year=year)
    if month:
        qs = qs.filter(date__month=month)
    total = sum(
        o.amount for o in qs)  # there is a better way to do this (aggregation)
    return render(request, "expenses/expense_list.html", {
        'year': year,
        'month': month,
        'total': total,
        'objects': qs,
    })


def detail(request, id):
    o = get_object_or_404(models.Expense, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.expense = o
            comment = form.save()
            messages.success(request, "Comment added successfully.")
            return redirect(
                "{}#comment-{}".format(o.get_absolute_url(), comment.id))

        messages.error(request, "Please fix errors in form.")

    else:
        form = CommentForm()

    return render(request, "expenses/expense_detail.html", {
        'object': o,
        'form': form,
    })


def create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect(reverse("expenses:detail", args=(o.id,)))
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })


def update(request, id):
    o = get_object_or_404(models.Expense, id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES, instance=o)
        if form.is_valid():
            o = form.save()
            return redirect(reverse("expenses:detail", args=(o.id,)))
    else:
        form = ExpenseForm(instance=o)

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })


def send_feedback(request):
    if request.method == "POST":
        form = FeebackForm(request.POST)
        if form.is_valid():
            print("feeback sent", form.cleaned_data)
            return redirect(reverse("expenses:list"))
    else:
        form = FeebackForm()

    return render(request, "expenses/feedback_form.html", {
        'form': form,
    })
