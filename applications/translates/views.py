import os

import openai
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from applications.base.response import operation_failure

from google.cloud import translate_v2 as translate
from google.cloud import vision

# Create your views here.


class ChatGPTAPIView(APIView):

    def post(self, request):
        text = request.data.get("text", None)
        if not text:
            return operation_failure

        question_text = f"{text}에 돼지고기가 들었다면 O, 들어있지 않다면 X로만 반환해줘. 다른 말 절대 하지말고"
        openai.api_key = settings.OPENAI_API_KEY
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                       messages=[{"role": "user", "content": question_text}])

        resposne_text = chat_completion.choices[0].message.content
        if "O" in resposne_text:
            return Response("porcinam continet.")
        else:
            return Response("porcinam non continet.")


class GoogleTranslateViewSet(GenericViewSet):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_APPLICATION_CREDENTIALS

    @action(methods=["POST"], detail=False, url_path="ocr")
    def vision_ocr(self, request):
        image = request.data.get("image", None)
        if not image:
            return operation_failure

        try:
            client = vision.ImageAnnotatorClient()
            content = image.read()

            ocr_image = vision.Image(content=content)

            response = client.text_detection(image=ocr_image)
            texts = response.text_annotations
            bounds_list = []

            for text in texts:
                vertices = [
                    [vertex.x, vertex.y] for vertex in text.bounding_poly.vertices
                ]

                bounds_list.append(vertices)

            return Response(bounds_list)
        except Exception as e:
            print(e)
            return operation_failure

    @action(methods=["POST"], detail=False, url_path="translate")
    def translate(self, request):
        text = request.data.get("text", None)
        if not text:
            return operation_failure

        try:
            translate_client = translate.Client()
            result = translate_client.translate(text, target_language="la")
            return Response(result)
        except Exception as e:
            print(e)
            return operation_failure
