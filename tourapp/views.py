from django.shortcuts import render
from .models import tourModel
from .models import feedbackModel

# Create your views here.
def tourism(request):
    tour_sites = tourModel.objects.all()
    feedback = feedbackModel.objects.all()
    context = {
        "sites": tour_sites,
        "feeds": feedback,
    }
    return render(request, 'tourism.html', context)

