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
@api_view(["POST"])
def sample(request):
    logger.info("info-inside sample views")
    logger.debug("debug-inside sample views")
    logger.error("error-inside sample views")
    logger.warning("warning-inside sample views")
    try:
        data=json.loads(request.body)
        return JsonResponse(data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)