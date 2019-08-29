from django.urls import path
from testEndPoint import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('s/', views.s_list),
    path('s/<int:pk>/', views.s_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)