from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to="expenses/", null=True, blank=True)

    def __str__(self):
        return "[#{}] ${} @{} {}".format(
            self.id,
            self.amount,
            self.date,
            self.title or "---"
        )

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id,))
