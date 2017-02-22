from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        # fields = "__all__"
        exclude = (
            'expense',
        )


class ExpenseSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = models.Expense
        # fields = (
        #     'id',
        #     'user',
        #     'title',
        #     'comments',
        # )
        fields = "__all__"
        depth = 1
