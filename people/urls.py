from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r"persons", views.PersonViewSet)
router.register(r"notes", views.NoteViewSet)

urlpatterns = [path("", include(router.urls))]
