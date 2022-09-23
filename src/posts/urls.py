from django.urls import path
from posts.views import BlogHome

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view, name='home'),
]