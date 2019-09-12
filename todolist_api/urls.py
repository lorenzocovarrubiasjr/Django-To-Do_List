from django.urls import path 
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('re/', views.re, name='re'),
    path('3/', views.all_items, name='all_items'),
    path('4/', views.create_item, name='create_item'),
    path('5/', views.delete_item, name='delete_item'),
    path('6/', views.quit, name='quit'),
    path('todolist/new/', views.new_todolist, name="new_todolist"),
    path('todolist/<id>/add', views.add_item, name="add_item"),
    path('todolist/<id>/incomplete', views.incomplete_items, name="incomplete_items"),
    path('todolist/<id>/complete', views.complete_items, name="complete_items"),
    path('todolist/<id>/', views.find_list_by_id, name="find_list_by_id"),
    path('todolist/', views.all_todolists, name="all_todolists"),
    path('todoitem/<id>/toggle', views.toggle_item, name="toggle_item"),
    path('todoitem/', views.all_todoitems, name="all_todoitems"),
]
