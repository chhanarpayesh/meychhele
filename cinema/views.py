from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import View
from django.core.urlresolvers import reverse
from django.views.generic import (TemplateView, ListView, 
    DetailView, CreateView, UpdateView)
from .models import (CinemaBook, DesignShot, FoodShot, LocationShot, Beginnings, Endings)
from .forms import (CinemaBookCreateForm, CinemaBookUpdateForm, DesignShotForm, FoodShotForm, LocationShotForm, BeginningsForm, EndingsForm)
from django.shortcuts import render, get_object_or_404

class CinemaListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        slug=self.kwargs.get("slug")
        if slug:
            queryset = CinemaBook.objects.filter(
            Q(verify=True) &
            Q(owner=self.request.user)
            )
        else:
            queryset = CinemaBook.objects.filter(owner=self.request.user)

        return queryset

class CinemaDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return CinemaBook.objects.filter(owner=self.request.user)

class CinemaCreateView(LoginRequiredMixin, CreateView):
    form_class=CinemaBookCreateForm
    login_url="/login/"
    template_name='cinema/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(CinemaCreateView, self).form_valid(form)

class CinemaUpdateView(LoginRequiredMixin, UpdateView):
    form_class=CinemaBookUpdateForm
    login_url="/login/"
    template_name='cinema/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(CinemaUpdateView, self).get_context_data(*args, **kwargs)
        # context for jinja templates
        name = self.get_object().name
        ctx['formtitle'] = 'Update Cinema: <span style="font-family:Abril Fatface">{}<span>'.format(name)
        return ctx

    def get_queryset(self):
        return CinemaBook.objects.filter(owner=self.request.user)

class DesignListView(ListView):
    def get_queryset(self):
        queryset = DesignShot.objects.filter(owner=self.request.user)
        return queryset

class DesignShotUpdateView(LoginRequiredMixin, UpdateView):
    model=DesignShot
    fields = ['cinema','dimage']
    template_name='cinema/form.html'

    def get_context_data(self, **kwargs):
        ctx = super(DesignShotUpdateView, self).get_context_data(**kwargs)
        cinema = self.get_object().cinema
        ctx['formtitle'] = 'Update Designs of <span style="font-family:Abril Fatface">{}<i>'.format(cinema)
        return ctx

class DesignShotCreateView(LoginRequiredMixin, CreateView):
    form_class=DesignShotForm
    login_url="/login/"
    template_name='cinema/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        render(self.request, self.template_name, self.get_context_data(form=form))
        return super(DesignShotCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(DesignShotCreateView, self).get_form_kwargs()
        # only show cinemas created by user
        kwargs['user']=self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(DesignShotCreateView, self).get_context_data(**kwargs)
        # context for jinja templates
        ctx['formtitle'] = 'Add a Design shot'
        return ctx

class FoodListView(ListView):
    def get_queryset(self):
        queryset = FoodShot.objects.filter(owner=self.request.user)
        return queryset

class FoodShotUpdateView(LoginRequiredMixin, UpdateView):
    model=FoodShot
    fields = ['cinema', 'fimage']
    template_name='cinema/form.html'

    def get_context_data(self, **kwargs):
        ctx = super(FoodShotUpdateView, self).get_context_data(**kwargs)
        cinema = self.get_object().cinema
        ctx['formtitle'] = 'Update Foods of <span style="font-family:Abril Fatface">{}<span>'.format(cinema)
        return ctx

class FoodShotCreateView(LoginRequiredMixin, CreateView):
    form_class=FoodShotForm
    login_url="/login/"
    template_name='cinema/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        render(self.request, self.template_name, self.get_context_data(form=form))
        return super(FoodShotCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(FoodShotCreateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(FoodShotCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add a Food shot'
        return ctx

class LocationListView(ListView):
    def get_queryset(self):
        queryset = LocationShot.objects.filter(owner=self.request.user)
        return queryset

class LocationShotUpdateView(LoginRequiredMixin, UpdateView):
    model=LocationShot
    fields = ['cinema', 'limage']
    template_name='cinema/form.html'
    
    def get_context_data(self, **kwargs):
        ctx = super(LocationShotUpdateView, self).get_context_data(**kwargs)
        cinema = self.get_object().cinema
        ctx['formtitle'] = 'Update Locations of <span style="font-family:Abril Fatface">{}<span>'.format(cinema)
        return ctx

class LocationShotCreateView(LoginRequiredMixin, CreateView):
    form_class=LocationShotForm
    login_url="/login/"
    template_name='cinema/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        render(self.request, self.template_name, self.get_context_data(form=form))
        return super(LocationShotCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(LocationShotCreateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(LocationShotCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add a Scenery shot'
        return ctx

class BeginningsListView(ListView):
    def get_queryset(self):
        queryset = Beginnings.objects.filter(owner=self.request.user)
        return queryset

class BeginningsCreateView(LoginRequiredMixin, CreateView):
    form_class=BeginningsForm
    login_url="/login/"
    template_name='cinema/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        render(self.request, self.template_name, self.get_context_data(form=form))
        return super(BeginningsCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(BeginningsCreateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(BeginningsCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Beginnings of Movies'
        return ctx

class BeginningsUpdateView(LoginRequiredMixin, UpdateView):
    model = Beginnings
    fields = ['scenes', 'lines']
    template_name='cinema/form.html'
    
    def get_context_data(self, **kwargs):
        ctx = super(BeginningsUpdateView, self).get_context_data(**kwargs)
        cinema = self.get_object().cinema
        ctx['formtitle'] = 'Beginning of <span style="font-family:Abril Fatface">{}<span>'.format(cinema)
        return ctx

class EndingsListView(ListView):
    def get_queryset(self):
        queryset = Endings.objects.filter(owner=self.request.user)
        return queryset

class EndingsCreateView(LoginRequiredMixin, CreateView):
    form_class=EndingsForm
    login_url="/login/"
    template_name='cinema/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        render(self.request, self.template_name, self.get_context_data(form=form))
        return super(EndingsCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super(EndingsCreateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(EndingsCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Endings of Movies'
        return ctx

class EndingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Endings
    fields = ['scenes', 'lines']
    template_name='cinema/form.html'

    def get_context_data(self, **kwargs):
        ctx = super(EndingsUpdateView, self).get_context_data(**kwargs)
        cinema = self.get_object().cinema
        ctx['formtitle'] = 'Ending of <span style="font-family:Abril Fatface">{}<span>'.format(cinema)
        return ctx
