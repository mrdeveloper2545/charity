
from django import forms
from .models import OnlineMember
from django_countries.widgets import CountrySelectWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class OnlineRegistrationForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'Not Specified')),initial='NOT_SPECIFIED',widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = OnlineMember
        fields = ['first_name', 'last_name', 'email','phone_number', 'gender', 'country']

        widgets = {
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
