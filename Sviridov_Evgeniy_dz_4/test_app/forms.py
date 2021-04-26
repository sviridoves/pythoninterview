from django.forms import ModelForm
from .models import Good_Item


class AddItemForm(ModelForm):
    class Meta:
        model = Good_Item
        fields = ('title', 'price', 'measure', 'vendor')
