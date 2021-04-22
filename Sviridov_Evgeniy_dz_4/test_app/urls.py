from django.urls import path
from .views import item_list_view, add_item

urlpatterns = [
    path('additem/', add_item),
    path('', item_list_view),
]
