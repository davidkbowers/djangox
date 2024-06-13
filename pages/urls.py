from django.urls import path

from .views import HomePageView, AboutPageView, BlogPageView, ClassesPageView, CommunityPageView, ContactPageView, ShopPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("classes/", ClassesPageView.as_view(), name="classes"),  
    path("community/", CommunityPageView.as_view(), name="community"),
    path("contact/", ContactPageView.as_view(), name="contact"),   
    path("shop/", ShopPageView.as_view(), name="shop"), 
]
