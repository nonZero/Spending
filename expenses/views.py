from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

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


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = "__all__"


def create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect(reverse("expenses:detail", args=(o.id,)))
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {
        'form' : form,
    })


SUBJECTS = (
    ("error", "Error in site"),
    ("attention", "I need attention"),
    ("other", "Other"),
)


class FeebackForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    phone = forms.CharField(required=False)


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
