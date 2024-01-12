from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="todo"),
    path('save-todo',SAVETODO,name="savetodo"),
    path('mark-complete/<int:id>',UPDATETODO,name="mark-complete"),
    path('delete-todo/<int:id>',DELETETODO,name="delete-todo"),
]