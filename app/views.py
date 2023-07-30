from django.shortcuts import render, redirect
from app.forms import produtosForm
from app.models import produtos
# Create your views here.
def home (request):
    data = {}
    data['db'] = produtos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = produtosForm()
    return render(request, 'form.html', data)

def create(request):
    form = produtosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = produtos.objects.get(pk=pk)
    data['form'] = produtosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = produtos.objects.get(pk=pk)
    form = produtosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')