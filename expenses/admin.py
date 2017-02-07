from django.contrib import admin
from . import models

class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date',
        'amount',
    )
    search_fields = (
        'id',
        'title',
        'date',
        'amount',
        'description',
    )
    date_hierarchy = 'date'

admin.site.register(models.Expense, ExpenseAdmin)