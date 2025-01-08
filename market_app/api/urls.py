from django.urls import path
from .views import MarketsView, market_single_view, sellers_view

urlpatterns = [
    path('markets/', MarketsView.as_view()),
    path('market/<int:pk>/', market_single_view, name='market-detail'),
    path('seller', sellers_view),
]