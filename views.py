from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Device, Model, Manufacturer
# from .tables import DeviceTable
# from .forms import SelectManufacturer, SelectModel
from .forms import selectDevice



# Create your views here.
def index(request):
    return render(request, "devmng/index.html", {'content': selectDevice})


def all_by_manufacturer(request, manufacturer_id):
    pass
    # table = Device.objects.filter(manufacturer=manufacturer_id)
    # return render(request, "devmng/index.html", {'content':table})

@csrf_exempt
def load_models(request):
    manufacturer_id = request.POST.get('manufacturer')
    models = Model.objects.filter(manufacturer=manufacturer_id).order_by('model')
    return render(request, 'devmng/model_dropdown_list_options.html', {'models': models})
