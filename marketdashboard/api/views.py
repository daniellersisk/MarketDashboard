from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Instrument
from .serializers import InstrumentSerializer

class InstrumentListView(APIView):
    def get(self, request):
        instrument = Instrument.objects.all()
        instrument_serializer = InstrumentSerializer(instrument, many=True)
        return Response(instrument_serializer.data)
