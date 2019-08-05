from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name = "bab"

urlpatterns = [
    path('browserecipes/',views.browserecipes, name = "browserecipes"),
    path('contact/',views.contact, name = "contact"),
    path('recipepage/<int:id>/',views.recipepage, name = "recipepage"),
    path('submitrecipe/',views.submitrecipe, name = "submitrecipe"),
    path('postcreate/',views.postcreate, name="postcreate"),
    path('like_toggle/<int:id>/', views.like_toggle, name="like_toggle"),
    path('post_like/', views.post_like, name="post_like"),    
    path('favorite_toggle/<int:post_id>/', views.favorite_toggle, name="favorite_toggle"),
    path('favorite/<int:user_id>/', views.favorite, name="favorite"),
    
]