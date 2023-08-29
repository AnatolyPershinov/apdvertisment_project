from django.urls import path
from .views import index, advertisement_post, advertisement_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('advertisement-post/', advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail')
]
