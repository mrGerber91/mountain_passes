from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .database_manager import DataBaseManager


class SubmitDataView(APIView):
    def post(self, request, format=None):
        # Проверяем, что данные POST-запроса содержат необходимые поля
        required_fields = ['date_added', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time',
                           'winter_level', 'summer_level', 'autumn_level', 'spring_level', 'coord_id', 'user_id']
        for field in required_fields:
            if field not in request.data:
                return Response({'error': f'Missing field: {field}'}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем данные из POST-запроса
        data = [
            request.data['date_added'],
            request.data['beauty_title'],
            request.data['title'],
            request.data['other_titles'],
            request.data['connect'],
            request.data['add_time'],
            request.data['winter_level'],
            request.data['summer_level'],
            request.data['autumn_level'],
            request.data['spring_level'],
            request.data['coord_id'],
            request.data['user_id'],
            'new'  # Устанавливаем значение поля status равным 'new'
        ]

        # Инициализируем объект базы данных и добавляем перевал
        db_manager = DataBaseManager()
        db_manager.connect()
        db_manager.add_pereval(data)
        db_manager.close()

        return Response({'message': 'Pereval added successfully'}, status=status.HTTP_201_CREATED)