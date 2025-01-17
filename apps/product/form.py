from django import forms

# creating a form
class CreateProductForm(forms.Form):
    number = forms.IntegerField()
