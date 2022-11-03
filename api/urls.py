from django.urls import path
from api.infrastructure.views import ApiClient
from django.views.generic import TemplateView

app_name = 'api'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('data', ApiClient.as_view(), name="get_data"),
    path('data/<str:imageId>', ApiClient.as_view())
]