
from django.urls import path
from .import views

urlpatterns = [
    path('create_task',views.create_task,name='create_task'),
    path('update_task/<int:id>',views.update_task,name='update_task'),
    path('delete_task/<int:id>',views.delete_task,name='delete_task'),
    path('read_task',views.read_task,name='read_task'),
]
