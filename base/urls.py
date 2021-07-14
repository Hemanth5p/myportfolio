from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name="home"),
    path('project/<str:pk>/', views.projectpage, name="project"),
    path('addproject/', views.addproject, name="addproject"),
    path('editproject/<str:pk>/',views.editproject,name="editproject"),
    path('inbox/',views.inboxpage,name="inbox"),
    path('message/<str:pk>/',views.messagepage,name="message"),
]
