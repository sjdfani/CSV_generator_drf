from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
import csv
from .serializer import csv_serializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from config.settings import BASE_DIR


class CSV_File(APIView):
    # permission_classes = [IsAdminUser]

    def get(self, request):
        data = dict()
        seri = csv_serializer(User.objects.all(), many=True)
        with open('csv_file.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(seri.data[0])
            print((seri.data[0]))
            for user in seri.data:
                writer.writerow(user.values())
        data['file'] = BASE_DIR + "csv_file.csv"
        return Response(data,status=status.HTTP_200_OK)
