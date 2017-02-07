from django.test import TestCase
from . import models


class ExpensesTests(TestCase):
    def test_basic_expense(self):
        n = models.Expense.objects.count()

        o = models.Expense(
            date="2012-04-22",
            amount="15.23",
            title="Pizza",
            description="For My birthday\nOlive + Mushroom.",
        )
        o.full_clean()
        o.save()

        self.assertEquals(n + 1,  models.Expense.objects.count())


