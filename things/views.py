from .models import Thing
from .serializers import ThingSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

class ThingList(ListAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveAPIView):
    queryset = Thing.objects()
    serializer_class = ThingSerializer