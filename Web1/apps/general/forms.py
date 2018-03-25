from django import forms

class PosibleClienteForm(forms.Form):
    RUC = forms.CharField(label = 'RUC', max_length = 12)
    nombre = forms.CharField(max_length = 100)
    email = forms.CharField(max_length = 150)
    telefono = forms.CharField(max_length = 15)
