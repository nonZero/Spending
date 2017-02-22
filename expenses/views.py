import decimal

import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from expenses.forms import ExpenseForm, FeebackForm, CommentForm
from . import models


# def my_view(request):
#     return HttpResponse("Shalom")


# class MyView(View):
#     def get(self, request):
#         return HttpResponse("Shalom")
#
#     # def post(self, request):
#     #     return HttpResponse("Shalom")

def my_view(request):
    return render(request, "my.html", {
        'colors': ['red', 'green', 'blue'],
        'result': time.time() // 100,
    })


class MyView(TemplateView):
    template_name = "my.html"

    colors = ['red', 'green', 'blue']

    def result(self):
        return time.time() % 100 // 1

    def get_context_data(self, **kwargs):
        d = super().get_context_data(bar=456, **kwargs)
        d['foo'] = 123
        return d


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class ExpenseListView(ListView):
#     model = models.Expense
#
# class CategoryListView(ListView):
#     model = models.Category
#
# class CommentListView(ListView):
#     model = models.Comment



@login_required
def list_months(request):
    qs = models.Expense.objects.filter(
        user=request.user
    ).dates('date', 'month').order_by('-date')
    return render(request, "expenses/expense_months.html", {
        'dates': qs,
    })


@login_required
def list(request, year=None, month=None):
    qs = models.Expense.objects.filter(user=request.user)
    if year:
        qs = qs.filter(date__year=year)
    if month:
        qs = qs.filter(date__month=month)
    term = request.GET.get('q')
    if term:
        q = Q(
            title__icontains=term
        ) | Q(
            description__icontains=term
        )
        try:
            q |= Q(amount=decimal.Decimal(term))
        except decimal.InvalidOperation:
            pass
        if term.isdigit():
            q |= Q(amount__gte=int(term), amount__lt=int(term) + 1)
        qs = qs.filter(q)

    total = sum(
        o.amount for o in qs)  # there is a better way to do this (aggregation)
    return render(request, "expenses/expense_list.html", {
        'year': year,
        'month': month,
        'total': total,
        'objects': qs,
        'term': term,
    })


@login_required
def detail(request, id):
    o = get_object_or_404(models.Expense, id=id, user=request.user)
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


# @login_required
# def create(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         form.fields['categories'].queryset = request.user.categories.all()
#         if form.is_valid():
#             form.instance.user = request.user
#             o = form.save()
#             return redirect(reverse("expenses:detail", args=(o.id,)))
#     else:
#         form = ExpenseForm()
#         form.fields['categories'].queryset = request.user.categories.all()
#
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })
#

class ExpenseEditView(LoginRequiredMixin):
    form_class = ExpenseForm
    model = models.Expense

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['categories'].queryset = self.request.user.categories.all()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        resp = super().form_valid(form)
        messages.success(self.request, self.message)
        return resp


class ExpenseCreateView(ExpenseEditView, CreateView):
    message = "Expense created!!!!!!"


class ExpenseUpdateView(ExpenseEditView, UpdateView):
    message = "Expense updated!!!!!!"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# @login_required
# def update(request, id):
#     o = get_object_or_404(models.Expense, id=id, user=request.user)
#     if request.method == "POST":
#         form = ExpenseForm(request.POST, request.FILES, instance=o)
#         form.fields['categories'].queryset = request.user.categories.all()
#         if form.is_valid():
#             o = form.save()
#             return redirect(reverse("expenses:detail", args=(o.id,)))
#     else:
#         form = ExpenseForm(instance=o)
#         form.fields['categories'].queryset = request.user.categories.all()
#
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })




@login_required
def delete(request, id):
    o = get_object_or_404(models.Expense, id=id, user=request.user)

    if request.method == "POST":
        o.delete()
        messages.success(request,
                         "Expense #{} deleted successfully.".format(id))
        return redirect(reverse("expenses:list"))

    return render(request, "expenses/expense_confirm_delete.html", {
        'object': o,
    })


# def send_feedback(request):
#     if request.method == "POST":
#         form = FeebackForm(request.POST)
#         if form.is_valid():
#             print("feeback sent", form.cleaned_data)
#             return redirect(reverse("expenses:list"))
#     else:
#         form = FeebackForm()
#
#     return render(request, "expenses/feedback_form.html", {
#         'form': form,
#     })
#

class FeedbackView(FormView):
    form_class = FeebackForm
    template_name = "expenses/feedback_form.html"
    success_url = reverse_lazy("expenses:list")

    def form_valid(self, form):
        messages.success(self.request, "Feedback Sent!!!!!!")
        return super().form_valid(form)
