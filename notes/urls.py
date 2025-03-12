from django.contrib import admin
from django.urls import path
from .views import note_list, note_create, note_detail, note_edit

urlpatterns = [
    path("list/", note_list, name="note_list"),
    path("create/", note_create, name="note_create"),
    path("list/<int:pk>/", note_detail, name="note_detail"),
    path("edit/<int:pk>/", note_edit, name="note_edit"),
]
