from django import forms

from Cleanzy.accounts.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class CreateAccountForm(AccountForm):
    pass


class DeleteAccountForm(AccountForm):
    pass


class EditAccountForm(AccountForm):
    pass


class LoginAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']

