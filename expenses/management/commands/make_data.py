import random

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
                date="2012-{:02}-{}".format(random.randint(1, 12),
                                            random.randint(1, 30)),
                amount="{:.2f}".format(random.uniform(1, 100)),
                title="Title #{}".format(i + 1),
                description="Desc " * i,
            )
            o.full_clean()
            o.save()
