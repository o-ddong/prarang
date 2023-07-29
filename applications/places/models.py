from django.db import models

from applications.base.models import BaseModel


# Create your models here.


class Pray(BaseModel):
    title = models.CharField(max_length=255, verbose_name="제목")
    createdtime = models.CharField(max_length=255, verbose_name="한국관광공사 내용 등록일")
    modifiedtime = models.CharField(max_length=255, verbose_name="한국관광고사 내용 수정일")
    areacode = models.CharField(max_length=255, verbose_name="위치 코드")
    sigungucode = models.CharField(max_length=255, verbose_name="시군구 코드")
    latitude = models.CharField(max_length=255, verbose_name="위도")
    longitude = models.CharField(max_length=255, verbose_name="경도")
    cat1 = models.CharField(max_length=255, verbose_name="타겟?")
    zipcode = models.CharField(max_length=255, verbose_name="우편번호")
    address = models.CharField(max_length=255, verbose_name="주소")


class Restaurant(BaseModel):
    region = models.CharField(max_length=255, verbose_name="지역")
    title = models.CharField(max_length=255, verbose_name="상호")
    food_type = models.CharField(max_length=255, verbose_name="음식 종류")
    address = models.CharField(max_length=255, verbose_name="주소")
    contact = models.CharField(max_length=255, verbose_name="연락처")
    menu = models.CharField(max_length=255, verbose_name="메뉴")
    price = models.CharField(max_length=255, verbose_name="가격")
    description = models.CharField(max_length=255, verbose_name="비고")



