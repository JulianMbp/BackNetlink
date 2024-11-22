from django.urls import path
from django.contrib import admin
from .views import PublicacionView
from .models import publicacion

admin.site.register(publicacion)
#url de publicacion
urlpatterns = [
    path('publicacion_list', PublicacionView.as_view()),
    path('publicacion_create', PublicacionView.as_view()),
    path('publicacion_update/<int:pkid>', PublicacionView.as_view(), name='publicacion_update'),
    path('publicacion_delete/<int:pkid>', PublicacionView.as_view(), name='publicacion_delete'),
]