from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=False, widget=forms.HiddenInput())
    email = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
