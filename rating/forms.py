from django.forms import ModelForm
from rating.models import Contact, Rating


class ContactForm(ModelForm):
    """
    Contact Us Form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'detail']


class RatingForm(ModelForm):
    """
    Rating Form
    """
    class Meta:
        model = Rating
        field = ['user', 'celebrity', 'rate', 'review']


