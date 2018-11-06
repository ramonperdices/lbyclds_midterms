from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import MyForm
# Create your views here.



def Home(request):
    return render(request, 'services/Home.html')
def maps(request):
    if request.method == 'POST':
        form = MyForm(request.POST) # if post method then form will be validated
        if form.is_valid():
            cd = form.cleaned_data
            longitude = cd.get('longitude')
            latitude = cd.get('latitude')
            form = MyForm()
            context = {
                'form': form,
                'longitude': longitude,
                'latitude': latitude,
            }
            return render(request, 'services/maps.html', context)
        else:
            # if sum not equal... then redirect to custom url/page
            return HttpResponseRedirect('/')  # mention redirect url in argument

    else:
        form = MyForm() # blank form object just to pass context if not post method
        longitude = -34.397
        latitude = 150.644
        context = {
            'form': form,
            'longitude': longitude,
            'latitude': latitude,
        }
    return render(request, 'services/maps.html', context)
