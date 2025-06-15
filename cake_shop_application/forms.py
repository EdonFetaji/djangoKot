from django import forms

from .models import Cake


class CakeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # super(CakeForm, self).__init__(args, kwargs)

        for field_name, field in self.fields.items():
            # if not isinstance(field,forms.widgets.TextInput):
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Cake
        exclude = ('baker',)
