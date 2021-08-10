from django.urls import path,re_path 
from author import views

urlpatterns = [ 
    re_path(r'^author', views.Author.as_view(), ),
    # re_path(r'^upAuthorInfo', views.upAuthorInfo, ),
    # re_path(r'^upAuthorName', views.upAuthorName, ),
]