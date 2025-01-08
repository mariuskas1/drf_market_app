from rest_framework import serializers
from market_app.models import Market, Seller


class MarketSerializer(serializers.HyperlinkedModelSerializer):    

    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Market
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        exclude = []

    def get_market_count(self, obj):
        return obj.markets.count()
        




