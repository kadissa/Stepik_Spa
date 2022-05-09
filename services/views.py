from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView, DetailView
from . import models


class Main(ListView):
    def get(self, request, *args, **kwargs):
        spa_s = models.Spa.objects.all()
        entries = models.Entry.objects.all()
        paginator = Paginator(spa_s, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj, 'entries': entries}
        return render(request, 'services/home.html', context)


def listing(request):
    spa = models.Spa.objects.all()
    paginator = Paginator(spa, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services/spa.html', context={'page_obj': page_obj})


class MassageView(ListView):
    model = models.Massage
    paginate_by = 3
    template_name = 'services/massage.html'


class Index(ListView):
    model = models.Spa
    template_name = 'services/index.html'


class MassageDetailView(View):
    # model = models.Massage
    # slug_url_kwarg = 'slag'
    # template_name = 'services/massage_detail.html'
    def get(self, request, slug):
        massage = get_object_or_404(models.Massage, slug=slug)
        return render(request, 'services/massage_detail.html', context={'massage': massage})


class SpaDetailView(View):
    def get(self, request, slug):
        spa = get_object_or_404(models.Spa, slag=slug)
        return render(request, 'services/spa_detail.html', context={'spa': spa})
