from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Dein Name:", max_length=120)