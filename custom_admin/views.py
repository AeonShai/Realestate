# custom_admin/views.py
from django.shortcuts import render, redirect
from .models import Ilan
from .forms import IlanForm

# İlanları listeleme
def ilan_list(request):
    ilanlar = Ilan.objects.all()
    return render(request, 'custom_admin/ilan_list.html', {'ilanlar': ilanlar})

# İlan ekleme
def ilan_add(request):
    if request.method == 'POST':
        form = IlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ilan_list')
    else:
        form = IlanForm()
    return render(request, 'custom_admin/ilan_form.html', {'form': form})

# İlan düzenleme
def ilan_edit(request, pk):
    ilan = Ilan.objects.get(pk=pk)
    if request.method == 'POST':
        form = IlanForm(request.POST, instance=ilan)
        if form.is_valid():
            form.save()
            return redirect('ilan_list')
    else:
        form = IlanForm(instance=ilan)
    return render(request, 'custom_admin/ilan_form.html', {'form': form})

# İlan silme
def ilan_delete(request, pk):
    ilan = Ilan.objects.get(pk=pk)
    ilan.delete()
    return redirect('ilan_list')
