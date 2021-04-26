from django.shortcuts import render
from .models import Good_Item
from .forms import AddItemForm


def item_list_view(request):
    return render(request, "item_index.html", {'object_list': Good_Item.objects.all()})


def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, "item_index.html", {'object_list': Good_Item.objects.all()})
    else:
        form = AddItemForm()
        return render(request, "add_item.html", {'form': form})
