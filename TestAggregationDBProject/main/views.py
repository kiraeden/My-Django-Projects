from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Products, Model, Versions, HLTP, MLTP, Test_Case_Inventory

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'index'
    queryset = Products.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['product_names'] = self.queryset
        return context
    
class ReleaseView(generic.DetailView):
    template_name = 'main/release.html'
    model = Versions

    def get_context_data(self, **kwargs):
        context = super(ReleaseView, self).get_context_data(**kwargs)
        context['product_names'] = Products.objects.all()
        return context
    
class ModelsView(generic.DetailView):
    template_name = 'main/models.html'
    model = Model
    
    def get_context_data(self, **kwargs):
        context = super(ModelsView, self).get_context_data(**kwargs)
        context['product_names'] = Products.objects.all()
        return context

class DataView(generic.DetailView):
    template_name = 'main/data.html'
    model = Model
    
    def get_context_data(self, **kwargs):
        context = super(DataView, self).get_context_data(**kwargs)
        context['product_names'] = Products.objects.all()
        context['hltp'] = HLTP.objects.all()
        context['mltp'] = MLTP.objects.all()
        context['tci'] = Test_Case_Inventory.objects.all()
        return context
    