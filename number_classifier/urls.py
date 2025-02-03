from django.urls import path
from .views import NumberClassifierView

urlpatterns = [
    path('classify-number', NumberClassifierView.as_view(), name='classify-number'),
]