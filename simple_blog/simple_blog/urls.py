"""simple_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog.views import MultipleBlogView, SimpleBlogDetailView, SimpleBlogView, BlogApiView
from blog.views_api import BlogListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path("api/blog/", BlogApiView.as_view(), name="blog-api-list"),
    path("api/blogs/", BlogListAPIView.as_view(), name="blog-rest-api-list"),

    path("blog/", MultipleBlogView.as_view(), name="blog-list"),
    path("blog/<int:blog_id>", SimpleBlogView.as_view(), name="simple-blog"),
    path(
        "blog/detail/<int:id>",
        SimpleBlogDetailView.as_view(),
        name="simple-detail-blog",
    ),
]
