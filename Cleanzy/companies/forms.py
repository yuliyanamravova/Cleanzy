from django import forms

from Cleanzy.companies.models import Company


class CompanyBaseForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)
        labels = {
            'name': 'Name',
            'address': 'Address',
            'vat_uic_number': 'VAT/UIC',
            'phone_number': 'Phone Number'
        }


class AddCompanyForm(CompanyBaseForm):
    pass


class DeleteCompanyForm(CompanyBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True


class EditCompanyForm(CompanyBaseForm):
    pass

