from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer


def get_item(pk):
    item = get_object_or_404(Item, pk=pk)
    if item:
        data = ItemSerializer(item)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # return Response({'message': "Wrong Id!", 'status_code': 406}, status=status.HTTP_406_NOT_ACCEPTABLE)


def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def patch_item(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data, partial=True)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

