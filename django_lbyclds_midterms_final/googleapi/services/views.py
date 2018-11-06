from django.shortcuts import render
# Create your views here.



def Home(request):
    return render(request, 'services/Home.html')
def maps(request):
    return render(request, 'services/maps.html')
