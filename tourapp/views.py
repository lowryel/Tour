from django.shortcuts import render, redirect
from .models import tourModel
from .models import feedbackModel
from .forms import feedbackForm

# Create your views here.


def tourism(request):
    tour_sites = tourModel.objects.all()
    feedback = feedbackModel.objects.all()

    if request.method == "POST":
        form = feedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('tourism')
    else:
        form = feedbackForm()
    context = {
        "sites": tour_sites,
        "feeds": feedback,
        "form": form
    }
    return render(request, 'tourism.html', context)
