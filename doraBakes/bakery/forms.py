from django import forms
from .validators import validate_number, validate_specialchar


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'robertdunsey'}))
    password = forms.CharField(label="Password", max_length=12, widget=forms.PasswordInput(attrs={'placeholder': '********'}))


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=20, help_text='15 characters max.', widget=forms.TextInput(attrs={'placeholder': 'Robert'}))
    email = forms.EmailField(label="Email", max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'robbie.email@email.com'}))
    username = forms.CharField(label="Username", max_length=15, help_text='15 characters max.', widget=forms.TextInput(attrs={'placeholder': 'robertdunsey'}))
    password = forms.CharField(label="Password", min_length=9, max_length=12, validators=[validate_number, validate_specialchar], widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    cPassword = forms.CharField(label="Confirm Password", help_text='This must match the previous password field.', widget=forms.PasswordInput(attrs={'placeholder': '********'}))

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cPassword')

        if password and cpassword and password != cpassword:
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data

