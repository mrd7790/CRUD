from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers
from rest_framework import status


@api_view()
def ApiOverview(request):
    api_urls = {
        'all_items': 'item/getAll',
        # 'Search by Category': '/?category=category_name',
        # 'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/item/create',
        'Update': '/item/update/pk',
        'Delete': '/item/delete/pk'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_item(request):
    item = ItemSerializer(data=request.data)

    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def add_items(request):
#     for data in request.data:
#         add_item(data)
#     return


@api_view(['POST'])
def add_items(request, self, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_param.dict())
    else:
        items = Item.objects.all()

    # if there is something in items else raise error
    if items:
        data = ItemSerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def view_items(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)