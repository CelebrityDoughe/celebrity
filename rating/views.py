from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from rating.models import Celebrity


class CategoryView(ListView):
    """
    View to render page for each category
    """

    #template_name = "category.html"
    model = Celebrity
    categories = ['actors', 'musicians', 'tv', 'radio', 'sports', 'politicians']

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
    #template_name = "celebrity.html"

