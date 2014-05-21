from django.forms import ModelForm
from rating.models import Rating


class RatingForm(ModelForm):
    """
    Rating Form
    """
    class Meta:
        model = Rating
        fields = ('rate', 'review')
