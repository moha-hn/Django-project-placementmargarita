from django.urls import path

from . import views

urlpatterns = [
    #main website
    path("esp/", views.indexesp, name="indexesp"),
    path("", views.indexfr, name="indexfr"),
    path("formesp/", views.formesp, name="formesp"),
    path("formfr/", views.formfr, name="formfr"),
    path("emploifr/", views.emploifr, name="emploifr"),
    path("emploiesp/", views.emploiesp, name="emploiesp"),
    path("contactesp/", views.contactesp, name="contactesp"),
    path("contactfr/", views.contactfr, name="contactfr"),

    #login
    path('login/',views.login_view,name='login'),
]