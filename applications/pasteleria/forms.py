from django import forms

from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.ChoiceField(choices=[('ProblemaConCompra','Problema con compra'),('Cotizacion','Cotizacion'),('Otro','Otro')])
    content = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()