from .serializers import MarketSerializer, SellerSerializer, ProductSerializer
from market_app.models import Market, Seller, Product
from rest_framework import generics, viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MarketsViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class SellersViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer




class SellerOfMarketList(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk = pk)
        return market.sellers.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk = pk)
        serializer.save(markets=[market])



