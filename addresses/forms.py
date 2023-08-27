from django import forms


class AddressForm(forms.Form):
    address = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'myform'



