from django import forms
from .widgets import CustomClearableFileInput
from works.models import Work, Content
from .models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'
    
    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        contents = Content.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
