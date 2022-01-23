from apscheduler.schedulers.background import BackgroundScheduler
from django.contrib.auth.models import User
from .serializer import csv_serializer
import csv


def csv_updater():
    seri = csv_serializer(User.objects.all(), many=True)
    with open('csv_file.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(seri.data[0])
        for user in seri.data:
            writer.writerow(user.values())


def main():
    sched = BackgroundScheduler(timezone='MST')
    sched.add_job(csv_updater, 'interval', minutes=1)
    sched.start()
