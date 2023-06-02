from django.urls import path
from .views import *

urlpatterns = [
    path('',traineelist,name='traineelist'),
    path('Add',traineeadd,name='traineeadd'),
    path('Update/<int:ID>',traineeupdate,name='traineeupdate'),
    path('Delete/<int:ID>',traineeDelete,name='traineeDelete'),
    path('list',traineelist,name='traineelist'),
]
