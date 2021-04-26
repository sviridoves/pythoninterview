from django.urls import path
from .views import item_list_view, add_item

app_name = 'test_app'
urlpatterns = [
    path('additem/', add_item, name='additem'),
    path('', item_list_view, name='index'),
]
