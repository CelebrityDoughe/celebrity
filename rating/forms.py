from django.forms import ModelForm
from rating.models import Contact


class ContactForm(ModelForm):
    """
    Contact Us Form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'detail']

