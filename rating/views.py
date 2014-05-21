# -*- coding: utf-8 -*-
from django.db.models import Avg
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from .forms import RatingForm
from .models import Celebrity, Rating


class CategoryView(LoginRequiredMixin, ListView):
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


class CelebrityDetailView(LoginRequiredMixin, FormView):
    """
    Detail page of Celebrity
    """

    template_name = 'rating/celebrity_detail.html'
    form_class = RatingForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CelebrityDetailView, self).get_context_data(**kwargs)
        celebrity = Celebrity.objects.get(slug=self.kwargs['slug'])
        context['celebrity'] = celebrity
        context['user'] = self.request.user
        try:
            # rating = Rating.objects.get(user=self.request.user, celebrity=celebrity)  # noqa
            context['rate_exist'] = True
        except Rating.DoesNotExist:
            context['rate_exist'] = False
        rating_count = Rating.objects.filter(celebrity=celebrity).count()
        rating_avg = Rating.objects.filter(celebrity=celebrity).aggregate(Avg('rate')).values()[0]  # noqa
        context.update({'rating_count': rating_count,
                        'rating_avg': rating_avg})
        return context

    def form_valid(self, form):
        form.save()
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
