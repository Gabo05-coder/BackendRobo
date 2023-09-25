from django import forms

class acForms(forms.Form):
    opciones = forms.ChoiceField(choices=[('Auto', 'Auto'), ('Manual', 'Manual')])
