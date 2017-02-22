from rest_framework import viewsets
from . import models
from . import serializers


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Expense.objects.all().order_by('-date')
    serializer_class = serializers.ExpenseSerializer
