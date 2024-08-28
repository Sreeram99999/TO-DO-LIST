from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('list',views.list,name='list'),
    path('details <int:pk>',views.details,name='details'),
    path('edit <int:pk>',views.edit,name='edit'),
    path('history',views.history,name='history'),
    path('mark <int:pk>',views.mark,name='mark'),
    path('delete <int:pk>',views.delete,name='delete'),
    path('contact',views.contact,name='contact')
]