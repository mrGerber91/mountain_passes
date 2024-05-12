from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer


@api_view(['POST'])
def submit_data(request):
    if request.method == 'POST':
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            pereval_added = serializer.save()
            return Response({
                "status": HTTP_200_OK,
                "message": "Отправлено успешно",
                "id": pereval_added.id
            })
        return Response({
            "status": HTTP_400_BAD_REQUEST,
            "message": "Bad Request",
            "id": None
        })
    return Response({
        "status": HTTP_500_INTERNAL_SERVER_ERROR,
        "message": "Ошибка при выполнении операции",
        "id": None
    })

@api_view(['GET'])
def get_single_data(request, id):
    try:
        pereval = PerevalAdded.objects.get(id=id)
        serializer = PerevalAddedSerializer(pereval)
        return Response(serializer.data)
    except PerevalAdded.DoesNotExist:
        return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def edit_data(request, id):
    try:
        pereval = PerevalAdded.objects.get(id=id)
        if pereval.status == 'new':
            serializer = PerevalAddedSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1, "message": "Успешно отредактировано"})
            return Response({"state": 0, "message": "Неверные данные для редактирования"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"state": 0, "message": "Нельзя редактировать запись"}, status=status.HTTP_403_FORBIDDEN)
    except PerevalAdded.DoesNotExist:
        return Response({"state": 0, "message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)

