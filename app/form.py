from django import forms

class Loginform(forms.Form):
    UserName = forms.CharField()
    PassWord = forms.CharField()