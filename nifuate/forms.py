from django import forms
from .models import OnlineMember
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries import countries  

class OnlineMemberForm(forms.ModelForm):
    class Meta:
        model = OnlineMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
  
        self.fields['first_name'].label = "First Name"
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['last_name'].label = "Last Name"
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['gender'].label = "Gender"
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})

        self.fields['email'].label = "Email"
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['country'].label = "Country"
        self.fields['country'].widget = forms.Select(choices=list(countries), attrs={'class': 'custom-select'})  


        self.fields['phone_number'] = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(
                attrs={'class': 'custom-select'},  
                
            )
        )
