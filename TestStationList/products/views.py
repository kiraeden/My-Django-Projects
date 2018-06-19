from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Products
from django.http.response import HttpResponse, HttpResponseRedirect

class ProductView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products'
    
class AddProductView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'products/addProduct.html'
    
class EditProductView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Products
    template_name = 'products/editProduct.html'
    context_object_name = 'product'
    
def addProduct(request):
    if request.user.is_authenticated:
        try:
            product = Products(product_name=request.POST['product_name'])
        except Exception as e:
            print(e)
            return HttpResponse(status=404)
        else:
            product.save()
            return HttpResponseRedirect('/products/index/')
    else:
        return HttpResponse(status=401)
        

def editProduct(request):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=request.POST['id'])
        try:
            product.product_name = request.POST['product_name']
        except Products.DoesNotExist:
            return HttpResponse(status=404)
        else:
            product.save()
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)
            
def deleteProduct(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            product = get_object_or_404(Products, pk=request.POST['id'])
            try:
                product.delete()
            except Products.DoesNotExist:
                return HttpResponse(status=404)
            else:
                return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)