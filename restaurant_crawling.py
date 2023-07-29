import csv
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from applications.places.models import Pray, Restaurant



with open("csv/restaurant_20181231.csv", 'r', encoding='utf-8') as f:
    print(f)
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        Restaurant.objects.create(
            region=row[0],
            title=row[1],
            food_type=row[2],
            address=row[3],
            contact=row[4],
            menu=row[5],
            price=row[6],
            description=row[7],
        )
