from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import logging
logger = logging.getLogger(__name__)

logger.info("Checking the status")
# Create your views here.
@api_view(["GET"])
def sample(request):
    logger.info("info-inside sample views hello")
    logger.debug("debug-inside sample views")
    logger.error("error-inside sample views")
    logger.error("192.109.130.111 - - \"GET /api HTTP/1.1\" 200 305 \"-\" \"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36\"")
    logger.error("[11:50:53 ERR] {\"Info\":{\"LoggerId\":\"1a7206fa-85fjalkjeflk554890af4\",\"Environment\":\"Production\",\"ServerName\":\"London\",\"ApplicationName\":\"Service\",\"TimeStamp\":\"04/01/2020 11:50:53\",\"Type\":\"Warning\",\"Message\":{\"Message\":\"DB connection Failed. Using Default Keys\",\"ClientName\":\"Client\",\"ClientId\":\"Client\",\"MessageType\":\"Configuration\"}},\"ErrorDetails\":{\"ClassName\":\"CloudService\",\"Message\":\"Error in Connection String\"}}")
    logger.warning("warning-inside sample views")
    try:
        #data=json.loads(request.body)
        return JsonResponse({"msg":"hello csk"})
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)