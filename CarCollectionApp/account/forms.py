from django import forms

from CarCollectionApp.account.models import ProfileModel


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ProfileModel
        fields = ['username', 'email_address', 'age', 'password']


class AccountEditForm(AccountForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
