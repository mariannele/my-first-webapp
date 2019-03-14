from django.shortcuts import render, redirect
from .models import Businesstrip
from .forms import BusinesstripForm


def HomePageView(request):
    return render(request, 'home.html', {})

def list_businesstrips(request):
     businesstrips = Businesstrip.objects.all()
     return render(request, 'businesstrips.html', {'businesstrips': businesstrips})

def create_businesstrip(request):
    form = BusinesstripForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_businesstrips')
    
    return render(request, 'businesstrip-form.html', {'form' : form})

def update_businesstrip(request, id):
    businesstrip = Businesstrip.objects.get(id=id)
    form = BusinesstripForm(request.POST or None, instance=businesstrip)

    if form.is_valid():
        form.save()
        return redirect('list_businesstrips')

    return render(request, 'businesstrip-form.html', {'form': form, 'businesstrip': businesstrip})

def delete_businesstrip(request, id):
    businesstrip = Businesstrip.objects.get(id=id)

    if request.method == 'POST':
        businesstrip.delete()
        return redirect('list_businesstrips')

    return render(request, 'businesstrip_delete.html', {'businesstrip' : businesstrip})
