from django.http import HttpResponse
from django.shortcuts import render

from . import models

def list(request):
    qs = models.Expense.objects.all()  # !!!!! QuerySet
    return render(request, "expenses/expense_list.html", {
        'objects': qs,
    })

# TODO: 1. create a detail() view function, on /23/ that shows all expense info
# TODO: 2. Link from list view <a href="....">click me</a> and back

