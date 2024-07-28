from django import forms 
from .models import Profile

class CvForm(forms.ModelForm): 
    class Meta: 
        model = Profile
        fields = ['name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills']