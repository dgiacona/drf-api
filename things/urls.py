from django.urls import path
from .views import ThingList, ThingDetail

urlpatterns = [
    path("", ThingList.as_view(), name="Thing_List"),
    path("<int:pk>/", ThingDetail.as_view(), name="Thing_detail"),
]