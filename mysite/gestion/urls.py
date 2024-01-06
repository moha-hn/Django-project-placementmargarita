from django.urls import path

from . import views

urlpatterns = [
    #admin panel
    path("admin/", views.admin, name="admin"),
    path("createjob/", views.createjob, name="createjob"),
    path('logout/',views.logout_view ,name='logout'),
    path('updatejob/<str:pk>/', views.updatejob , name="updatejob"),
    path('deletejob/<str:pk>/', views.deletejob , name="deletejob"),
]