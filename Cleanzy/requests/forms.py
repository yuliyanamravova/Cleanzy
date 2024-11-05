from django import forms

from Cleanzy.requests.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class CreateRequestForm(RequestForm):
    class Meta:
        model =Request
        exclude = ('author', 'date', )


class EditRequestForm(RequestForm):
    pass


class DeleteRequestForm(RequestForm):
    pass
