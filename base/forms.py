from django import forms
from .models import found_child_data


class found_child_data_form(forms.ModelForm):

    class Meta:
        model = found_child_data
        fields = '__all__'
