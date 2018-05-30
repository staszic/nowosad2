from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_title = forms.CharField(required=True)
    contact_msg = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Imię:"
        self.fields['contact_email'].label = "Adres e-mail:"
        self.fields['contact_title'].label = "Temat:"
        self.fields['contact_msg'].label = "Treść wiadomości:"
