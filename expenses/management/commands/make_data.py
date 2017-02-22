import datetime
import random

import silly
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from expenses import models
from expenses.models import Category


def get_random_date():
    while True:
        try:
            return datetime.date(
                random.randint(2010, 2019),
                random.randint(1, 12),
                random.randint(1, 30)
            )
        except ValueError:
            # non existent date
            pass


def get_paragraph(a, b):
    """
    Produces a paragraph of text with between a and b sentences.
    """
    return "\n".join([silly.sentence() for x in range(random.randint(a, b))])


class Command(BaseCommand):
    help = "Adds demo data to database."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        n = options['n']

        users = []
        for i in range(1, 6):
            user, created = User.objects.get_or_create(
                username='user{}'.format(i),
            )
            cats = list(user.categories.all())
            if not cats:
                cats = [user.categories.create(name=silly.noun()) for i in range(5)]

            user.set_password("secret1234")
            user.save()
            users.append(user)

        for i in range(n):
            with transaction.atomic():
                o = models.Expense(
                    user=random.choice(users),
                    date=get_random_date(),
                    amount="{:.2f}".format(random.uniform(1, 100)),
                    title="{} {}".format(silly.adjective(), silly.noun()).title(),
                    description=get_paragraph(1, 3),
                )
                o.full_clean()
                o.save()
                sample = set(random.sample(cats, random.randint(1, 3)))
                for cat in sample:
                    o.categories.add(cat)

                for i in range(random.randint(0, 5)):
                    o.comments.create(
                        content=get_paragraph(1, 4),
                    )
