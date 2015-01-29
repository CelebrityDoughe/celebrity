# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Max
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import SuperuserRequiredMixin

from .forms import SliderItemForm
from .models import Slider, SliderItem


class SliderCreateView(SuperuserRequiredMixin, CreateView):
    model = Slider
    success_url = reverse_lazy('sliders:list')


class SliderDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Slider
    success_url = reverse_lazy('sliders:list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class SliderListView(SuperuserRequiredMixin, ListView):
    model = Slider


class SliderItemListView(SuperuserRequiredMixin, ListView):
    model = SliderItem

    def get_queryset(self):
        qs = super(SliderItemListView, self).get_queryset()
        slider = Slider.objects.get(pk=self.kwargs['slider_pk'])
        return qs.filter(slider=slider).order_by('index')

    def get_context_data(self, **kwargs):
        data = super(SliderItemListView, self).get_context_data(**kwargs)
        slider = Slider.objects.get(pk=self.kwargs['slider_pk'])
        data.update({'slider': slider})
        return data


class SliderItemCreateView(SuperuserRequiredMixin, CreateView):
    model = SliderItem
    form_class = SliderItemForm

    def get_success_url(self):
        return reverse('sliders:items', kwargs={'slider_pk': self.kwargs['slider_pk']})

    def get_context_data(self, **kwargs):
        data = super(SliderItemCreateView, self).get_context_data(**kwargs)
        data.update({'slider': Slider.objects.get(pk=self.kwargs['slider_pk'])})
        return data

    def form_valid(self, form):
        item = form.save(commit=False)
        item.slider = Slider.objects.get(pk=self.kwargs['slider_pk'])
        max_index = item.slider.slideritem_set.all().aggregate(Max('index'))['index__max']
        if not max_index:
            max_index = 0
        item.index = max_index + 1
        item.save()
        self.object = item
        return super(SliderItemCreateView, self).form_valid(form)


class SliderItemUpdateView(SuperuserRequiredMixin, UpdateView):
    model = SliderItem
    form_class = SliderItemForm

    def get_success_url(self):
        return reverse('sliders:items', kwargs={'slider_pk': self.kwargs['slider_pk']})

    def get_context_data(self, **kwargs):
        data = super(SliderItemUpdateView, self).get_context_data(**kwargs)
        data.update({'slider': Slider.objects.get(pk=self.kwargs['slider_pk'])})
        return data


class SliderItemDeleteView(SuperuserRequiredMixin, DeleteView):
    model = SliderItem

    def get_success_url(self):
        return reverse('sliders:items', kwargs={'slider_pk': self.kwargs['slider_pk']})

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
