from rest_framework.serializers import ModelSerializer
from core.models import Sellers

class SellersSerializer(ModelSerializer):
    class Meta:
        model = Sellers
        fields = '__all__'