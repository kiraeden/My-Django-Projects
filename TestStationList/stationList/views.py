from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from stationList.models import StationData

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = StationData
    template_name = 'stationList/index.html'
    context_object_name = 'StationData'

class AddView(LoginRequiredMixin, generic.FormView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = StationData
    template_name = 'stationList/addStation.html'

class EditView(LoginRequiredMixin, generic.FormView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = StationData
    template_name = 'stationList/editStation.html'

@login_required(redirect_field_name='redirect_to', login_url='/accounts/login/')
def checkout(request, station_id):
    if request.user.is_authenticated():
        station = get_object_or_404(StationData, pk=station_id)
        try:
            station.in_use_for = request.POST['Checkout_Reason']
        except StationData.DoesNotExist:
            # Redisplay the question voting form.
            return render(request, 'stationList/index.html', {
                'station': station,
                'error_message': "Something went wrong with your checkout request...",
            })
        else:
            station.checked_out = "{}.{}".format(request.user.first_name, request.user.last_name)
            station.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('stationList:index', args=(question.id,)))