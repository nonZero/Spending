import datetime
import random

import silly
from django.core.management.base import BaseCommand

from expenses import models


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


class Command(BaseCommand):
    help = "Adds demo data to database."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        n = options['n']
        for i in range(n):
            o = models.Expense(
                date=get_random_date(),
                amount="{:.2f}".format(random.uniform(1, 100)),
                title="{} {}".format(silly.adjective(), silly.noun()).title(),
                description=silly.paragraph(length=random.randint(1, 3)),
            )
            o.full_clean()
            o.save()
