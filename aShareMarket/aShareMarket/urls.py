from django.conf.urls import url
from ashareAll import views

urlpatterns = [
    url(r'^updatesStockAll/', views.updatesStockAll),
]
