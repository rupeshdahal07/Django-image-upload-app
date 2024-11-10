from django import forms
from .models import Image

class Imageform(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','image', 'description']
        labels = {
            'title': 'Title',
            'image': 'Image',
            'description': 'Description'
        }