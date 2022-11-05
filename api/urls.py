from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken import views

from api.infrastructure.views import ApiClient

app_name = 'api'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('data/<str:id>', ApiClient.as_view(), name="get_data"),
    path('data/update/', ApiClient.as_view(), name="post_data"),
    path('data/update/<str:id>', ApiClient.as_view(), name="put_data"),
    path('data/delete/<str:id>', ApiClient.as_view(), name="delete_data"),
    path('api-token-auth/', views.obtain_auth_token)
]
