from django import forms
from .models import * 

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'