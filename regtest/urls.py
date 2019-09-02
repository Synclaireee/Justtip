from django.urls import path
from regtest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('r/', views.S_List.as_view()),
    path('r/<int:pk>/', views.S_Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)