from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

admin.autodiscover()

from .views import main_page, resume

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter('')

urlpatterns = [
    path('', main_page),
]
urlpatterns += router.urls
