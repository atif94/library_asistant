from django import forms
from django.contrib.auth.forms import PasswordResetForm

class FancyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "you@example.com",
            "autocomplete": "email",
        })
    )
