from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiMain, name="main"),
    path('note_list/', views.noteList, name="note_list"),
    path('note_detail/<str:pk>/', views.noteDetail, name="note_detail"),
    path('note_create/', views.noteCreate, name="note_create"),
    path('note_update/<str:pk>/', views.noteUpdate, name="note_update"),
    path('note_delete/<str:pk>/', views.noteDelete, name="note_delete"),
]
