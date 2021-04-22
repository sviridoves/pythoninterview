from django.shortcuts import render
from .models import Good_Item


def item_list_view(request):
    return render(request, "item_index.html", {'object_list': Good_Item.objects.all()})


def add_item(request):
    return render(request, "add_item.html", {'form': 'Add Item'})
