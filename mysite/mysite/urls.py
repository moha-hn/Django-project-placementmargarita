
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #link urls from an app
    path("myapp/", include("myapp.urls")),
    path("gestion/", include("gestion.urls")),
]