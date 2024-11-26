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
    class Meta:
        model =Request
        exclude = ('author', 'date', )


class DeleteRequestForm(RequestForm):
    class Meta:
        model = Request
        exclude = ('author', 'date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True