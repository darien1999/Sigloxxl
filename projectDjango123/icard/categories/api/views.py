from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from categories.models import Category
from categories.api.serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    pagination_class = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
