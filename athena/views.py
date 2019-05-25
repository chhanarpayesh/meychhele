from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models.functions import Extract
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import AthenaCard, AthenaRank, AthenaVideoFile, AthenaImageFile
from .forms import AthenaCardCreateForm, AthenaCardUpdateForm, AthenaRankCreateForm, AthenaRankUpdateForm

from datetime import date

class AthenaListView(ListView):
    paginate_by = 13
    def get_queryset(self):
        slug=self.kwargs.get("slug")
        if slug in ['sa', 'wo']:
            queryset = AthenaCard.objects.filter(roots=slug)
        elif slug in ['f','m']:
            queryset = AthenaCard.objects.filter(status=slug)
        elif slug == 'll':
            queryset = AthenaCard.objects.filter(face=slug)
        elif slug == 'bb':
            queryset = AthenaCard.objects.filter(body=slug)
        elif slug == 'bazooka':
            queryset = AthenaCard.objects.filter(bazooka=True)
        elif slug == 'tushy':
            queryset = AthenaCard.objects.filter(tushy=True)
        elif slug == 'sortbydate':
            queryset = AthenaCard.objects.all().order_by('timestamp')
        elif slug == 'sortbyage':
            queryset = AthenaCard.objects.all().order_by('-dob')
        elif slug == 'sortbydaterev':
            queryset = AthenaCard.objects.all().order_by('-timestamp')
        elif slug == 'sortbyagerev':
            queryset = AthenaCard.objects.all().order_by('dob')
        elif slug == 'sortbyname':
            queryset = AthenaCard.objects.all().order_by('name')
        elif slug == 'sortbydob':
            queryset = AthenaCard.objects.annotate(
                birth_date_month = Extract('dob', 'month'), 
                birth_date_day = Extract('dob', 'day')
            ).order_by('birth_date_month', 'birth_date_day').all().exclude(dob=date(1989, 1, 1))
        elif slug == 'nodob':
            queryset = AthenaCard.objects.filter(incomplete=True)
        elif slug=='angel':
            queryset = AthenaCard.objects.filter(
                Q(bazooka=True) &
                Q(tushy=True)
            )
        elif slug=='goddess':
            queryset = AthenaCard.objects.filter(
                Q(face='ll') & 
                Q(body='bb') & 
                Q(bazooka=True) &
                Q(tushy=True)
            )
        elif slug:
            if 's-' in slug:
                xterm = slug.split('-')[1]
                term = ''.join(e for e in xterm if e.isalnum())
                queryset = AthenaCard.objects.filter(
                    Q(name__contains=term)
                )
        else:
            queryset = AthenaCard.objects.all()

        try:
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)


class AthenaListAllView(ListView):
    def get_queryset(self):
        queryset = AthenaCard.objects.all()
        return queryset


class AthenaDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return AthenaCard.objects.all()

    def get_context_data(self, *args, **kwargs):
        ctx = super(AthenaDetailView, self).get_context_data(*args, **kwargs)
        today = date.today()
        dob = self.get_object().dob
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        ctx['age'] = age
        return ctx

class AthenaCreateView(LoginRequiredMixin, CreateView):
    form_class=AthenaCardCreateForm
    login_url="/login/"
    template_name='athena/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance = form.save()
        files = self.request.FILES.getlist('vid')
        images = self.request.FILES.getlist('images')
        for f in files:
            AthenaVideoFile.objects.create(vid=f, athena=instance)
        for i in images:
            AthenaImageFile.objects.create(img=i, athena=instance)
        return super(AthenaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        ctx = super(AthenaCreateView, self).get_context_data(*args, **kwargs)
        ctx['formtitle'] = 'Create your Athena'
        return ctx

class AthenaUpdateView(LoginRequiredMixin, UpdateView):
    form_class=AthenaCardUpdateForm
    login_url="/login/"
    template_name='athena/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        files = self.request.FILES.getlist('vid')
        images = self.request.FILES.getlist('images')
        for f in files:
            AthenaVideoFile.objects.create(vid=f, athena=instance)
        for i in images:
            AthenaImageFile.objects.create(img=i, athena=instance)
        return super(AthenaUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        ctx = super(AthenaUpdateView, self).get_context_data(*args, **kwargs)
        naam = self.get_object().name
        ctx['formtitle'] = 'Update {0}'.format(naam)
        return ctx

    def get_queryset(self):
        return AthenaCard.objects.all()

class AthenaRankListView(ListView):
    def get_queryset(self):
        queryset = AthenaRank.objects.all()
        return queryset

class AthenaRankCreateView(LoginRequiredMixin, CreateView):
    form_class=AthenaRankCreateForm
    login_url="/login/"
    template_name='athena/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(AthenaRankCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        ctx = super(AthenaRankCreateView, self).get_context_data(*args, **kwargs)
        ctx['formtitle'] = 'Create a Rank'
        return ctx

class AthenaRankUpdateView(LoginRequiredMixin, UpdateView):
    form_class=AthenaRankUpdateForm
    login_url="/login/"
    template_name='athena/form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(AthenaRankUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        ctx = super(AthenaRankUpdateView, self).get_context_data(*args, **kwargs)
        ctx['formtitle'] = 'Update Rank #{0}'.format(self.get_object().rank)
        return ctx

    def get_queryset(self):
        return AthenaRank.objects.all()

# from djqscsv import render_to_csv_response
# def csv_view(request):
#   qs = AthenaCard.objects.all().order_by('name')
#   return render_to_csv_response(qs)