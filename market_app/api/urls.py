from django.urls import path
from .views import MarketsView, market_single_view, sellers_view, SellersView, MarketDetail

urlpatterns = [
    path('markets/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetail.as_view()),
    path('sellers/', SellersView.as_view()),
]