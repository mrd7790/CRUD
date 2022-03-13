from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status


@api_view()
def api_over_view(request):
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
    id_exists = request.data.get('id', 0)
    # validating for already existing data
    if id_exists:
        error_message = 'This payload cannot contain (id)'
        return Response(data=error_message,
                        status=status.HTTP_400_BAD_REQUEST)
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def add_items(request, self, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def item_manipulate(request, pk):
    if request.method == 'GET':
        return get_item(request, pk)
    elif request.method == 'PUT':
        return update_item(request, pk)
    elif request.method == 'PATCH':
        return patch_item(request, pk)
    elif request.method == 'delete':
        return delete_item(request, pk)


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


@api_view(['GET'])
def get_all_items(request):
    print('get all items')
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
