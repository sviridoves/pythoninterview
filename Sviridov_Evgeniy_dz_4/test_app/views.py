from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import serializers
from .models import Good_Item
from .forms import AddItemForm


def item_list_view(request):
    return render(request, "item_index.html", {'object_list': Good_Item.objects.all()})


def new_item_list_view(request):
    items = Good_Item.objects.all()
    if request.method == 'POST':
        form = AddItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_index_new'))
    else:
        form = AddItemForm()
    context = {'items': items, 'form': form}
    return render(request, "item_index_new.html", context=context)


def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_index_new'))
    else:
        form = AddItemForm()
    context = {'form': form}
    return render(request, "add_item.html", context=context)


def save_item_form(request):
    items = Good_Item.objects.all()
    data = serializers.serialize('json', items)
    return HttpResponse(data, content_type='text/html')
