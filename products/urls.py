from django.urls import path

from products.views import OwnerView

urlpatterns = [
    path('', OwnerView.as_view()),
]