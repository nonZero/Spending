from django.http import HttpResponse
from django.shortcuts import render

from . import models

def list(request):
    qs = models.Expense.objects.all()
    total = sum(o.amount for o in qs)  # there is a better way to do this (aggregation)
    return render(request, "expenses/expense_list.html", {
        'total': total,
        'objects': qs,
    })

def detail(request, id):
    o = models.Expense.objects.get(id=id)
    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })
