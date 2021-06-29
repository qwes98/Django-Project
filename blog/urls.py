from django.urls import path
from .views import index, post_list

urlpatterns = [
	path('', index),
	path('post/', post_list),
]
