from django.urls import path
from .views import MarketsView, SellersView, MarketDetail, SellerDetail, SellerOfMarketList

urlpatterns = [
    path('markets/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetail.as_view()),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('sellers/', SellersView.as_view()),
    path('seller/<int:pk>/', SellerDetail.as_view()),

]