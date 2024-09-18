from django.urls import path
from . import views

urlpatterns = [
    path('execute/', views.CodeExecutionView.as_view(), name='execute-code'),
]
