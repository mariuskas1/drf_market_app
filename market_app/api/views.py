from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import MarketSerializer, SellerSerializer
from market_app.models import Market, Seller
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics



class MarketsView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SellersView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





@api_view(['GET', 'DELETE', 'PUT'])
def market_single_view(request, pk):

    if request.method == 'GET':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market)
        return Response(serializer.data)
    
    
    if request.method == 'PUT':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
    
    if request.method == 'DELETE':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market)
        market.delete()
        return Response(serializer.data)
    

