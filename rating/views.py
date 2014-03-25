from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rating.models import Celebrity
from rating.forms import ContactForm


class CategoryView(ListView):
    """
    View to render page for each category
    """

    model = Celebrity
    categories = ['actors', 'musicians', 'tv', 'radio', 'sports', 'politicians']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryView, self).dispatch(*args, **kwargs)

    def get_category_shortcut(self, category):
        """
        Get first capital character of category as it would be used in Category model
        """
        keyword = category[0].upper()
        return keyword

    def get_queryset(self):
        category = self.kwargs['slug']
        if category and category in self.categories:
            keyword = self.get_category_shortcut(category)
            return Celebrity.objects.filter(specificity=keyword)
        return None

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['slug']
        return context


class CelebrityDetailView(DetailView):
    """
    Detail page of Celebrity
    """

    model = Celebrity

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CelebrityDetailView, self).dispatch(*args, **kwargs)


class ContactUsView(FormView):
    """
    Contact Us page
    """

    template_name = 'contact-us.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)


