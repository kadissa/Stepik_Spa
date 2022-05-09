from django.urls import path, include

from users import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.sign_up, name='sign_up')
]

