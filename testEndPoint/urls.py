from django.urls import path
from testEndPoint import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.S_List.as_view()),
    path('<int:pk>/', views.S_Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)