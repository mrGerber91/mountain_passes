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
            # Получаем валидные данные из сериализатора
            validated_data = serializer.validated_data

            # Создаем новый объект PerevalAdded и заполняем его данными из запроса
            pereval_added = PerevalAdded(
                beauty_title=validated_data['beauty_title'],
                title=validated_data['title'],
                other_titles=validated_data['other_titles'],
                connect=validated_data['connect'],
                add_time=validated_data['add_time'],
                user_email=validated_data['user']['email'],
                user_fam=validated_data['user']['fam'],
                user_name=validated_data['user']['name'],
                user_otc=validated_data['user']['otc'],
                user_phone=validated_data['user']['phone'],
                latitude=validated_data['coords']['latitude'],
                longitude=validated_data['coords']['longitude'],
                height=validated_data['coords']['height'],
                winter_level=validated_data['level']['winter'],
                summer_level=validated_data['level']['summer'],
                autumn_level=validated_data['level']['autumn'],
                spring_level=validated_data['level']['spring']
            )

            # Сохраняем новый объект PerevalAdded в базе данных
            pereval_added.save()

            # Возвращаем ответ с кодом 200 OK и информацией о успешном добавлении
            return Response({
                "status": HTTP_200_OK,
                "message": "Отправлено успешно",
                "id": pereval_added.id
            })

        # Возвращаем ответ с кодом 400 Bad Request в случае невалидных данных
        return Response({
            "status": HTTP_400_BAD_REQUEST,
            "message": "Bad Request",
            "id": None
        })

    # Возвращаем ответ с кодом 500 Internal Server Error в случае ошибки сервера
    return Response({
        "status": HTTP_500_INTERNAL_SERVER_ERROR,
        "message": "Ошибка при выполнении операции",
        "id": None
    })