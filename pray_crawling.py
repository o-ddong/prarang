import os
import django

import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from applications.places.models import Pray

from django.conf import settings

URL = settings.KOREA_TOURISM_ORGANIZATION_URL

data = {
    "serviceKey": settings.TOURISM_DECODING_KEY,
    "MobileOS": "IOS",
    "MobileApp": "prarang",
    "contentTypeId": 1146,
    "numOfRows": 1000,
    "_type": "json"
}

response = requests.get(f"{URL}", params=data)

data = response.json()
pray_infos = data["response"]["body"]["items"]["item"]

for info in pray_infos:
    if info['addr2']:
        info['addr1'] += f" {info['addr2']}"

    Pray.objects.create(
        title=info["title"],
        createdtime=info["createdtime"],
        modifiedtime=info["modifiedtime"],
        areacode=info["areacode"],
        sigungucode=info["sigungucode"],
        latitude=info["mapx"],
        longitude=info["mapy"],
        cat1=info["cat1"],
        zipcode=info["zipcode"],
        address=f"{info['addr1']}",
    )
