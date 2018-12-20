from django.conf.urls import url
from app import views

#url partterns of site tourism
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^setSite/', views.setSite.as_view()),
    url(r'^getSite/', views.getSite.as_view()),
    url(r'^getToken/', views.getToken.as_view()),
]