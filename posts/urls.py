from django.urls import path
from .views import first_post, posts_list

urlpatterns = [
    path('1', first_post),
    path('', posts_list)
]
