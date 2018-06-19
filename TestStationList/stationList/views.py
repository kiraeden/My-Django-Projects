from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from stationList.models import StationData
import datetime
from products.models import Products

class HomeView(generic.TemplateView):
    template_name = 'stationList/home.html'

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = StationData
    template_name = 'stationList/index.html'
    context_object_name = 'StationData'

class AddView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Products
    template_name = 'stationList/addStation.html'
    context_object_name = 'product_list'

class EditView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = StationData
    template_name = 'stationList/editStation.html'
    context_object_name = "station"
    
    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['product_list'] = Products.objects.all()
        return context

@login_required(redirect_field_name='redirect_to', login_url='/accounts/login/')
def check_out_station(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            station = get_object_or_404(StationData, pk=request.POST['id'])
            if station.checked_out == "No":
                try:
                    station.in_use_for = request.POST['checkout_reason']
                    station.checked_out = request.POST['username']
                except StationData.DoesNotExist:
                    return render(request, 'stationList/index.html', {
                        'error_message': "Something went wrong inside yo",
                    })
                else:
                    station.save()
                    return HttpResponse(status=202)
            else:
                return render(request, 'stationList/index.html',{
                        'error_message': "The PC was already checked out, you must release it before it can be checked out."
                    })
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)

@login_required(redirect_field_name='redirect_to', login_url='/accounts/login/')
def release_station(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            station = get_object_or_404(StationData, pk=request.POST['id'])
            if station.checked_out == "No":
                return render(request, 'stationList/index.html', {
                    'station': station,
                    'error_message': "The PC requested has already been released."
                })
            else:
                try:
                    station.checked_out = "No"
                    station.in_use_for = ""
                except StationData.DoesNotExist:
                    return render(request, 'stationList/index.html', {
                        'error_message': "The requested station object does not exist."
                    })
                else:
                    station.save()
                    return HttpResponse(status=202)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)

def edit_station(request):
    if request.user.is_authenticated:
        station = get_object_or_404(StationData, pk=request.POST['station_id'])
        if not str(station.pc_name).upper() == str(request.POST['pc_name']).upper():
            if StationData.objects.filter(pc_name = request.POST['pc_name']).exists():
                return render(request, 'stationList/editStation.html', {
                    'station': station,
                    'error_message': "The PC name field change was not the same as the existing field, and the new name was already in the database."
                })
        try:
            station.pc_name = request.POST['pc_name']
            station.location = request.POST['fixture_location']
            station.current_project = request.POST['project_name']
            station.working = request.POST['working']
            station.sspec = request.POST['sspec']
            station.clapper = request.POST['clapper']
            station.dac = request.POST['dac']
            station.pmd = request.POST['pmd']
            station.comment = request.POST['gen_comment']
            station.box_id = request.POST['box_id']
            station.pc_os = request.POST['pc_os']
            station.ip_address = request.POST['ip_address']
            station.mac_address = request.POST['mac_address']
            station.pc_port_num = request.POST['pc_port']
        except StationData.DoesNotExist:
            return render(request, 'stationList/editStation.html', {
                'station': station,
                'error_message': "Edit submission attempt replied with: station no longer exists...",
            })
        else:
            station.save()
            return HttpResponseRedirect(reverse('stationList:index'))
    else:
        return HttpResponse(status=401)
        
def add_station(request):
    if request.user.is_authenticated:
        if not StationData.objects.filter(pc_name=request.POST['pc_name']).exists():
            try:
                station = StationData()
                station.pc_name = request.POST['pc_name']
                station.location = request.POST['fixture_location']
                station.current_project = request.POST['project_name']
                station.working = request.POST['working']
                station.sspec = request.POST['sspec']
                station.clapper = request.POST['clapper']
                station.dac = request.POST['dac']
                station.pmd = request.POST['pmd']
                station.comment = request.POST['gen_comment']
                station.box_id = request.POST['box_id']
                station.pc_os = request.POST['pc_os']
                station.ip_address = request.POST['ip_address']
                station.mac_address = request.POST['mac_address']
                station.pc_port_num = request.POST['pc_port']
                station.maintenance = None
                station.maintainer = ""
                station.checked_out = "No"
            except StationData.DoesNotExist:
                return render(request, 'stationList/addStation.html', {
                    'station': station,
                    'error_message': "Add submission attempt replied with: station no longer exists...",
                })
            else:
                station.save()
                return HttpResponseRedirect(reverse('stationList:index'))
        else:
            return render(request, 'stationList/addStation.html', {
                    'error_message': "PC Name already exists in the database. Add request refused; please find and edit the existing station.",
            })
    else:
        return HttpResponse(status=401)
            
def delete_station(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            station = get_object_or_404(StationData, pk=request.POST['id'])
            try:
                station.delete()
            except StationData.DoesNotExist:
                return HttpResponse(status=404)
            except Exception as e:
                print(e)
                return HttpResponse(status=400)
            else:
                return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)
    
def update_maintenance(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            station = get_object_or_404(StationData, pk=request.POST['id'])
            try:
                station.maintenance = datetime.date.today()
                station.maintainer = request.POST['username']
            except StationData.DoesNotExist:
                return HttpResponse(status=404)
            except Exception as e:
                print(e)
                return HttpResponse(status=400)
            else:
                station.save()
                return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)
                