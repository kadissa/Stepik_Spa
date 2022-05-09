from django.urls import path
from . import views
# url services
urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    path('about', views.listing, name='spa'),
    path('massage', views.MassageView.as_view(), name='massage'),
    path('index', views.Index.as_view(), name='index'),
    path('massage_detail/<slug>/', views.MassageDetailView.as_view(), name='massage_detail'),
    path('spa_detail/<slug>', views.SpaDetailView.as_view(), name='spa_detail')
]
