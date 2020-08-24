from rest_framework.viewsets import ModelViewSet
from core.models import Sellers
from core.api.serializers import SellersSerializer


class SellersViewSet(ModelViewSet):
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer
    filter_fields = '__all__'