from django.urls import path
from peoples import views

urlpatterns = [
    path('peoples/', views.RegisterList.as_view()),
    path('peoples/<int:pk>', views.RegisterDetail.as_view()),
]
