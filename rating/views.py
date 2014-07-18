# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Avg
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from braces.views import AjaxResponseMixin, JSONResponseMixin

from .constants import CATEGORY_TITLE
from .forms import RatingForm
from .models import Celebrity, Rating


class CategoryView(ListView):
    """
    View to render page for each category
    """

    model = Celebrity

    def get_queryset(self):
        """
        Display celebrity by category
        """
        return Celebrity.objects.filter(specificity=self.kwargs['slug']).order_by('-average_rate')[:10]  # noqa

    def get_context_data(self, **kwargs):
        """
        Add extra data to context
        """
        data = super(CategoryView, self).get_context_data(**kwargs)
        data.update({'category': CATEGORY_TITLE[self.kwargs['slug']]})
        return data


class CelebrityDetailView(FormView):
    """
    Detail page of Celebrity
    """

    template_name = 'rating/celebrity_detail.html'
    form_class = RatingForm

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super(CelebrityDetailView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        """
        Redirect to the same page
        """
        return self.request.path

    def get_context_data(self, **kwargs):
        """
        Add extra data to context
        """
        context = super(CelebrityDetailView, self).get_context_data(**kwargs)
        celebrity = Celebrity.objects.get(slug=self.kwargs['slug'])

        my_rating = None
        if self.request.user.is_authenticated():
            my_ratings = Rating.objects.filter(celebrity=celebrity,
                                               user_id=self.request.user.id)
            if my_ratings.exists():
                my_rating = my_ratings[0]

        context.update({'celebrity': celebrity, 'my_rating': my_rating})
        return context

    def form_valid(self, form):
        """
        Save rating.
        """
        celebrity = Celebrity.objects.get(slug=self.kwargs['slug'])
        rating = form.save(commit=False)
        rating.celebrity = celebrity
        rating.user_id = self.request.user.id
        rating.save()
        celebrity.rate_count = Rating.objects.filter(celebrity=celebrity).count()  # noqa
        celebrity.average_rate = Rating.objects.filter(celebrity=celebrity).aggregate(Avg('rate')).values()[0]  # noqa
        celebrity.save()
        return super(CelebrityDetailView, self).form_valid(form)


class SearchView(AjaxResponseMixin, JSONResponseMixin, View):
    """
    Search View
    """
    def get_ajax(self, request, *args, **kwargs):
        """
        Search for ajax
        """
        keyword = self.request.REQUEST['keyword']
        celebrities = Celebrity.objects.filter(name__icontains=keyword)[:6]
        celebrities_json = []
        for cele in celebrities:
            celebrities_json.append({
                'label': cele.name,
                'url': reverse('rating:celebrity_detail', kwargs={'slug': cele.slug}),  # noqa
                'category': cele.get_specificity_display()})
        return self.render_json_response(celebrities_json)

    def get(self, request, *args, **kwargs):
        keyword = self.request.REQUEST.get('keyword', None)
        if keyword:
            objects = Celebrity.objects.filter(name__icontains=keyword)
            return render_to_response(
                'search-result.html',
                {'celebrities': objects, 'keyword': keyword},
                context_instance=RequestContext(self.request))

        return redirect("/")
