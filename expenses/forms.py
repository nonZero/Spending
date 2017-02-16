from django import forms

from expenses import models


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = "__all__"


class FeebackForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    phone = forms.CharField(required=False)
