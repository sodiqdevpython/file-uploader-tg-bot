from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import mainData, DocsData, DocsData2, DocsData3, DocsData4, DocsData5, DocsData6
from .serializers import (
    mainDataSerializer,
    DocsDataSerializer,
    DocsData2Serializer,
    DocsData3Serializer,
    DocsData4Serializer,
    DocsData5Serializer,
    DocsData6Serializer
)

@api_view(['GET', 'POST'])
def main_data_list(request):
    if request.method == 'GET':
        tg_id = request.GET.get('tg_id')
        if tg_id:
            data = mainData.objects.filter(tg_id=tg_id)
            serializer = mainDataSerializer(data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'POST':
        serializer = mainDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_data(request):
    tg_id = request.GET.get('tg_id')
    if tg_id:
        mainData.objects.filter(tg_id=tg_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def handle_upload(request, model, serializer_class, document_field):
    tg_id = request.data.get('tg_id')
    user = get_object_or_404(mainData, tg_id=tg_id)
    
    document_data = {document_field: request.FILES.get(document_field)}
    document_data['user'] = user.id
    
    doc_instance, created = model.objects.get_or_create(user=user)
    
    serializer = serializer_class(doc_instance, data=document_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'PUT'])
def upload_document(request):
    return handle_upload(request, DocsData, DocsDataSerializer, 'document')

@api_view(['POST', 'PUT'])
def upload_document2(request):
    return handle_upload(request, DocsData2, DocsData2Serializer, 'document2')

@api_view(['POST', 'PUT'])
def upload_document3(request):
    return handle_upload(request, DocsData3, DocsData3Serializer, 'document3')

@api_view(['POST', 'PUT'])
def upload_document4(request):
    return handle_upload(request, DocsData4, DocsData4Serializer, 'document4')

@api_view(['POST', 'PUT'])
def upload_document5(request):
    return handle_upload(request, DocsData5, DocsData5Serializer, 'document5')

@api_view(['POST', 'PUT'])
def upload_document6(request):
    return handle_upload(request, DocsData6, DocsData6Serializer, 'document6')
