from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^id/(?P<article_id>\d+)/$',views.article_by_id,name='id')
]