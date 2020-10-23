from . import views
from django.urls import include, path
from rest_framework import routers
from floppy import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet, basename='note')

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('edit/<int:note_id>/', views.edit),
    path('delete/<int:note_id>/', views.delete),
    path('api/', include(router.urls)),
]
