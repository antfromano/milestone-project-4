from django import forms
from .models import Work, Content


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        contents = Content.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in contents]

        self.fields['content'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
