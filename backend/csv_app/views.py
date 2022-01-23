from django.http import FileResponse, HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
import csv
from .serializer import csv_serializer
from django.contrib.auth.models import User


class CSV_File(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        seri = csv_serializer(User.objects.all(), many=True)
        try:
            with open('csv_file.csv', 'r+') as file:
                writer = csv.writer(file)
                writer.writerow(seri.data[0])
                for user in seri.data:
                    writer.writerow(user.values())
                file_data = file.read()
                response = HttpResponse(
                    file_data, content_type='application/csv_file.csv')
                response['Content-Disposition'] = 'attachment; filename="csv_file.csv"'
        except IOError:
            response = HttpResponseNotFound('<h1>File not exist</h1>')
        return response


def send_data(request):
    csv_file = open('csv_file.csv', 'r')
    request = FileResponse(csv_file)
    return request