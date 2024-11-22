import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from api_publicacion.models import publicacion
from .serializer import publicacion_serializer
from django.shortcuts import render
import base64

# Create your views here.
#Clase publicacion view
class PublicacionView(APIView):
    def get(self, request, *args, **kwargs):
            lista_publicaciones=publicacion.objects.all()
            serializer_publicaciones=publicacion_serializer(lista_publicaciones, many=True)
            return Response(serializer_publicaciones.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Leer y codificar el archivo multimedia en base64
        multimedia = request.FILES.get('multimedia')
        if multimedia:
            multimedia_bytes = multimedia.read()
            multimedia_base64 = base64.b64encode(multimedia_bytes).decode('utf-8')
        else:
            multimedia_base64 = None

        # Crear el diccionario con los datos
        data = {
            'titulo': request.data.get('titulo'),
            'descripcion': request.data.get('descripcion'),
            'multimedia': multimedia_base64,
        }

        # Usar el serializer para validar y guardar
        serializador = publicacion_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(
                {
                    "message": "Publicación creada con éxito",
                    "data": serializador.data,
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "message": "Error al crear publicación",
                    "data": serializador.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pkid):
        mi_publicacion=publicacion.objects.filter(id=pkid).update(
            titulo=request.data.get('titulo'),
            descripcion=request.data.get('descripcion'),
            multimedia=request.data.get('multimedia'),
        )
        return Response(mi_publicacion, status=status.HTTP_200_OK)
    def delete(self, request, pkid):
        mi_publicacion=publicacion.objects.filter(id=pkid).delete()
        return Response(mi_publicacion, status=status.HTTP_204_NO_CONTENT)
