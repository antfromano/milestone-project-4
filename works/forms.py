from django import forms
from .models import Work, Content


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        contents = Content.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
