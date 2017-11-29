from django.conf.urls import url
from . import views

app_name = "venta"


urlpatterns = [
    url(r'^$', views.index_dashboard, name="dashboard" )
]