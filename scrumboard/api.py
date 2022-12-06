from rest_framework.viewsets import ModelViewSet
from scrumboard.models import List, Card
# from scrumboard.serializers import ListSerializer, CardSerializer


""""
ModelViewSet allows GET PUT POST DELETE
"""
#
#
# class ListViewSet(ModelViewSet):
#     queryset = List.objects.all() # aici practic colectam toate obiectele din DB
#     serializer_class = ListSerializer # a se remarca mostenirea, se folosesc fnctionalitati din DRF(django rest fw)
#
#
# class CardViewSet(ModelViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer