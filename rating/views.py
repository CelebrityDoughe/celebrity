# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

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
        return Celebrity.objects.filter(specificity=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """
        Add extra data to context
        """
        data = super(CategoryView, self).get_context_data(**kwargs)
        data.update({'category': self.kwargs['slug']})
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
        rating_count = Rating.objects.filter(celebrity=celebrity).count()
        rating_avg = Rating.objects.filter(celebrity=celebrity).aggregate(Avg('rate')).values()[0]  # noqa

        my_rating = None
        if self.request.user.is_authenticated():
            my_ratings = Rating.objects.filter(celebrity=celebrity,
                                               user=self.request.user)
            if my_ratings.exists():
                my_rating = my_ratings[0]

        context.update({'rating_count': rating_count,
                        'rating_avg': rating_avg,
                        'celebrity': celebrity,
                        'my_rating': my_rating
                        })
        return context

    def form_valid(self, form):
        """
        Save rating.
        """
        rating = form.save(commit=False)
        rating.celebrity = Celebrity.objects.get(slug=self.kwargs['slug'])
        rating.user = self.request.user
        rating.save()
        return super(CelebrityDetailView, self).form_valid(form)


class SearchView(LoginRequiredMixin, View):
    """
    Search View
    """

    template_name = 'search-result.html'

    def post(self, *args, **kwargs):
        keyword = self.request.POST.get('keyword', None)
        if keyword:
            objects = Celebrity.objects.filter(name__icontains=keyword)
            return render_to_response(
                self.template_name,
                {'celebrities': objects, 'keyword': keyword},
                context_instance=RequestContext(self.request))

        return redirect("/")

    def get(self, *args, **kwargs):
        return redirect("/")
