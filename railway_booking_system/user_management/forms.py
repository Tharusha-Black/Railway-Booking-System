from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import FormActions
from django.forms.widgets import DateInput
from datetime import datetime
from django_countries.fields import CountryField
from .models import RailwayUser

class SignupForm(UserCreationForm):
    NIC = forms.CharField(max_length=12, label='NIC')
    email = forms.EmailField()
    registered_date = forms.DateField(initial=datetime.now().date(), widget=forms.HiddenInput())
    country = CountryField().formfield(label='Country')
    mobile_number = forms.CharField(max_length=15, label='Mobile Number')  # Changed to CharField
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = RailwayUser 
        fields = ['NIC','first_name', 'last_name', 'username', 'email', 'password1', 'password2',  'registered_date', 'country', 'mobile_number', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('NIC', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'username',
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('country', css_class='form-group col-md-4 mb-0'),
                Column('mobile_number', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            'registered_date',
            'date_of_birth',
            FormActions(
                Submit('submit', 'Sign up', css_class='btn btn-primary')
            )
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(
                Submit('submit', 'Login', css_class='btn btn-primary')
            )
        )
