from django.urls import path,re_path
from book import views

urlpatterns = [ 
    re_path(r'^book', views.Book.as_view(), ),
    # re_path(r'^upBookInfo', views.upBookInfo, ),
    # re_path(r'^upBookName', views.upBookName, ),
]