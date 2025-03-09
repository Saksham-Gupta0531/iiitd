from django.urls import path
from .views import ExecuteQueryAPIView

urlpatterns = [
    path('execute-query/', ExecuteQueryAPIView.as_view(), name='execute-query'),
]