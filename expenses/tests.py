from django.test import TestCase
from . import models


class ExpensesTests(TestCase):

    def create_expense(self):
        o = models.Expense(
            date="2012-04-22",
            amount="15.23",
            title="Pizza",
            description="For My birthday\nOlive + Mushroom.",
        )
        o.full_clean()
        o.save()

        return o

    def test_basic_expense(self):
        n = models.Expense.objects.count()
        o = self.create_expense()
        self.assertEquals(n + 1,  models.Expense.objects.count())
        o.delete()

    def test_comments(self):
        o = self.create_expense()

        c1 = models.Comment(
            expense=o,
            content="Hello!!!!",
        )
        c1.full_clean()
        c1.save()

        c2 = models.Comment.objects.create(
            expense=o,
            content="Hello 222222!!!!",
        )

        # qs = models.Comment.objects.filter(expense=o)
        # - euqals to -
        # qs = o.comment_set.all()
        qs = o.comments.all()

        self.assertEquals(qs.count(), 2)

        c3 = o.comments.create(
            content="Hello 22123213212222!!!!",
        )

        self.assertEquals(qs.count(), 3)
