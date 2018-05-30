from django.shortcuts import render, get_object_or_404
from .models import Plant


# Create your views here.
def index(request):
    plants_list = Plant.objects.order_by('category', 'plant_name')
    context = {'plants_list': plants_list}
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})