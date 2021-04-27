from django.urls import path
from .views import item_list_view, add_item, new_item_list_view

app_name = 'test_app'
urlpatterns = [
    path('additem/', add_item, name='additem'),
    path('new/', new_item_list_view, name='index_new'),
    path('', item_list_view, name='index'),
]
