from django import forms
from registro.models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
