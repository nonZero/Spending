from django.shortcuts import render, redirect
from django.urls import reverse

from expenses.forms import ExpenseForm, FeebackForm
from . import models


def list(request):
    qs = models.Expense.objects.all()
    total = sum(
        o.amount for o in qs)  # there is a better way to do this (aggregation)
    return render(request, "expenses/expense_list.html", {
        'total': total,
        'objects': qs,
    })


def detail(request, id):
    o = models.Expense.objects.get(id=id)
    return render(request, "expenses/expense_detail.html", {
        'object': o,
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
