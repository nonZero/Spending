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
        for i in range(n):
            o = models.Expense(
                date=get_random_date(),
                amount="{:.2f}".format(random.uniform(1, 100)),
                title="{} {}".format(silly.adjective(), silly.noun()).title(),
                description=get_paragraph(1, 3),
            )
            o.full_clean()
            o.save()
            for i in range(random.randint(0, 5)):
                o.comments.create(
                    content=get_paragraph(1, 4),
                )
