import random

import silly
from django.core.management.base import BaseCommand

from expenses import models


class Command(BaseCommand):
    help = "Adds demo data to database."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        n = options['n']
        for i in range(n):
            o = models.Expense(
                date="201{}-{:02}-{}".format(
                    random.randint(0, 9),
                    random.randint(1, 12),
                    random.randint(1, 30)
                ),
                amount="{:.2f}".format(random.uniform(1, 100)),
                title=silly.title(),
                description=silly.paragraph(length=random.randint(1, 3)),
            )
            o.full_clean()
            o.save()
