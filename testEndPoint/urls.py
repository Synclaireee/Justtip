from django.urls import path
from testEndPoint import views

urlpatterns = [
    path('s/', views.s_list),
    path('s/<int:pk>/', views.s_detail),
]