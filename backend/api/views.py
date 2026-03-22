from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import MenuItem, Order, OrderItem
from .serializers import MenuItemSerializer, OrderSerializer


class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for menu items"""
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category')
        if category:
            items = MenuItem.objects.filter(category=category, is_available=True)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        return Response({'error': 'Category parameter required'}, status=400)


class OrderViewSet(viewsets.ModelViewSet):
    """API endpoint for orders"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """Create a new order"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending orders"""
        pending_orders = Order.objects.filter(status='pending')
        serializer = self.get_serializer(pending_orders, many=True)
        return Response(serializer.data)
