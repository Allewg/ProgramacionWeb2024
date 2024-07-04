from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    try:
        item = Producto.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({'OK': True, 'msg': 'Producto eliminado con éxito.'})
    except Producto.DoesNotExist:
        return JsonResponse({'OK': False, 'msg': 'Producto no encontrado.'}, status=404)