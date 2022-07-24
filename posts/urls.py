from django.urls import path,include
from . import views


app_name = "posts"
urlpatterns = [

    # Class views urls
    path('',views.PostListView.as_view(),name="home"),
    path('<int:page>/',views.PostListView.as_view(),name = "home"),
    path('posts/<slug>',views.PostDetail.as_view(),name = "post"),
    path('Authors/<slug:phoneNumber>',views.AuthorDetail.as_view(),name = "author"),
    path('Authors/<slug:phoneNumber>/<int:page>',views.AuthorDetail.as_view(),name = "author"),
    # path('Category/<slug>',views.CategoryDetail.as_view(),name = "category"),
    # path('Category/<slug>/<int:page>',views.CategoryDetail.as_view(),name = "category"),
]
