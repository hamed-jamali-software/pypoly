from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path
from . import views
from .views import logout_view

from .views import (
    HomeView,
    PostUpdateView,
    PostDeleteView,
    AddPostView,
    SignupView,
    LoginInterfaceView,
    AuthorizedView,
    PostListView,

)



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),


    # User Authentication
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginInterfaceView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('authorized/', AuthorizedView.as_view(), name='authorized'),

]