from django import forms

from expenses import models


class ExpenseForm(forms.ModelForm):

    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['categories'].queryset = user.categories.all()


    class Meta:
        model = models.Expense
        exclude = (
            'user',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = (
            'content',
        )


class FeebackForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    phone = forms.CharField(required=False)
