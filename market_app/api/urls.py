from django.urls import path, include
from .views import SellerOfMarketList, ProductViewSet, MarketsViewSet, SellersViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)
router.register(r'markets', MarketsViewSet)  
router.register(r'sellers', SellersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view())
]