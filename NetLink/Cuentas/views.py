from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from Cuentas.models import laboralInformation
from django.db import models
from Cuentas.models import Experience, AcademicInformation, Usuario
from Cuentas.serializer import laboralInformationSerializer, academicInformationSerializer, experienceSerializer, usuarioSerializer
import base64
class laboralInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        laboralList = laboralInformation.objects.all()
        laboralSerializer = laboralInformationSerializer(laboralList, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def getLaboralInfo(self, request, id, *args, **kwargs):
        miLaboralInfo = laboralInformation.objects.filter(id = id).first()
        laboralSerializer = laboralInformationSerializer(miLaboralInfo, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        previousExperiences = []
        
        for i in request.data.get('previousExperiences'):
            experience = Experience.objects.create(company=i['company'],
                position= i['position'],
                description= i['description'])

            previousExperiences.append(experience.pk)
        
        data = {
            'latestPosition':request.data.get('latestPosition'),
            'abilities': request.data.get('abilities'),
            'previousExperiences': previousExperiences,
            'lookingForEmployement': request.data.get('lookingForEmployement'),
            'desiredPosition': request.data.get('desiredPosition'),
            'desiredCountry': request.data.get('desiredCountry'),
            'telecommuting': request.data.get('telecommuting')
        }
        
        serializer = laboralInformationSerializer(data=data)
        
        if serializer.is_valid():
            laboral_info = serializer.save()
            laboral_info.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class experienceApiView(APIView):
    def get(self, request, *args, **kwargs):
        eList = Experience.objects.all()
        eSerializer = experienceSerializer(eList, many=True)
        return Response(eSerializer.data, status=status.HTTP_200_OK)
    
    def getExperience(self, request, id, *args, **kwargs):
        miExperience = Experience.objects.filter(id = id).first()
        eSerializer = experienceSerializer(miExperience, many=True)
        return Response(eSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'company':request.data.get('company'),
            'position': request.data.get('position'),
            'description': request.data.get('description')
        }
        
        serializer = experienceSerializer(data=data)
        
        if serializer.is_valid():
            experience = serializer.save()
            experience.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid):
        try:
            experience = Experience.objects.get(id=pkid)
        except Experience.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        experience.save()

        serializer = experienceSerializer(experience)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pkid):
        try:
            experience = Experience.objects.get(id=pkid)
            
            experience.delete()
            
            return Response({"message": "Información laboral eliminada exitosamente."}, status=status.HTTP_200_OK)
        
        except Experience.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)

class academicInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        academicList = AcademicInformation.objects.all()
        academicSerializer = academicInformationSerializer(academicList, many=True)
        return Response(academicSerializer.data, status=status.HTTP_200_OK)
    
    def getAcademicInfo(self, request, id, *args, **kwargs):
        miAcademicInfo = AcademicInformation.objects.filter(id = id).first()
        academicSerializer = academicInformationSerializer(miAcademicInfo, many=True)
        return Response(academicSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'educativeInstitution':request.data.get('educativeInstitution'),
            'title':request.data.get('title'),
            'academicDiscipline':request.data.get('academicDiscipline'),
            'startDate':request.data.get('startDate'),
            'endDate':request.data.get('endDate'),
            'aditionalActivities': request.data.get('aditionalActivities'),
            'description': request.data.get('description'),
            'abilities': request.data.get('abilities')
        }
        
        serializer = academicInformationSerializer(data=data)
        
        if serializer.is_valid():
            laboral_info = serializer.save()
            laboral_info.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid, *args, **kwargs):
        try:
            academic = AcademicInformation.objects.get(id=pkid)
        except AcademicInformation.DoesNotExist:
            return Response({'error': 'Informacion no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        abilities = academic.abilities
        
        aditionalActivities = academic.aditionalActivities
        
        for i in request.data.get('abilities'):
            abilities.append(i)
            
        for i in request.data.get('aditionalActivities'):
            aditionalActivities.append(i)
        
        data = {
            'educativeInstitution':request.data.get('educativeInstitution'),
            'title':request.data.get('title'),
            'academicDiscipline':request.data.get('academicDiscipline'),
            'startDate':request.data.get('startDate'),
            'endDate':request.data.get('endDate'),
            'aditionalActivities': aditionalActivities,
            'description': request.data.get('description'),
            'abilities': abilities
        }
                
        serializer = academicInformationSerializer(academic,data=data, partial=True) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(request.data)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

class UsuariosView(APIView):
    def get(self, request, *args, **kwargs):
            lista_usuarios=Usuario.objects.all()
            serializer_usuarios=usuarioSerializer(lista_usuarios, many=True)
            return Response(serializer_usuarios.data,status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        
            # Leer y codificar el archivo de imagen en base64
            imagen = request.FILES.get('imagen')
            if imagen:
                imagen_bytes = imagen.read()
                imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')
            else:
                imagen_base64 = None  # Si no hay imagen, establecer como None
    
            # Crear el diccionario con los datos
            data = {
                'nombre': request.data.get('nombre'),
                'contrasena': request.data.get('contrasena'),
                'fechaNacimiento': request.data.get('fechaNacimiento'),
                'email': request.data.get('email'),
                'paisOrigen': request.data.get('paisOrigen'),
                'imagen': imagen_base64,  # Agregar la imagen codificada
            }
    
            # Usar el serializer para validar y guardar
            serializador = usuarioSerializer(data=data)
            if serializador.is_valid():
                serializador.save()  # Guardar el usuario
                return Response(
                    {"message": "Usuario creado correctamente", "data": serializador.data},
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {"message": "El usuario no se pudo crear", "errors": serializador.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    
    def put(self, request, pkid):
    # Intenta actualizar el usuario y guarda la cantidad de registros afectados
        registros_actualizados = Usuario.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            contrasena=request.data.get('contrasena'),
            fechaNacimiento=request.data.get('fechaNacimiento'),
            email=request.data.get('email'),
            paisOrigen=request.data.get('paisOrigen')
        )

    # Si se actualizó al menos un registro, devuelve un mensaje de éxito
        if registros_actualizados > 0:
            return Response(
                {"message": "Usuario actualizado correctamente"},
                status=status.HTTP_200_OK
        )
        else:
            return Response(
                {"message": "El usuario no se pudo actualizar"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pkid, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(id=pkid)
            usuario.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class UsuarioQueryApiView(APIView):
    def get(self, request, pkid, *args, **kargs):
        miUsuario=Usuario.objects.filter(id=pkid).first()
        serializer_usuario = usuarioSerializer(miUsuario)
        return Response(serializer_usuario.data, status=status.HTTP_200_OK)

class validateApiView(APIView):
    def post(self, request, *args, **kwargs):
        data={
            'email':request.data.get('email'),
            'contrasena':request.data.get('contrasena'),
        }
        if Usuario.objects.filter(email=data['email'], contrasena=data['contrasena']).exists():
            return Response(True, status=status.HTTP_200_OK) #ver perfil
        return Response(False, status=status.HTTP_400_BAD_REQUEST)
    
class CombinedInfoApiView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            # Obtener información laboral, filtrando por id
            laboral_info = laboralInformation.objects.filter(id=id).first()
            if not laboral_info:
                return Response({'error': 'Información laboral no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            laboral_serializer = laboralInformationSerializer(laboral_info)

            # Obtener información académica, filtrando por id
            academic_info = AcademicInformation.objects.filter(id=id).first()
            if not academic_info:
                return Response({'error': 'Información académica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            academic_serializer = academicInformationSerializer(academic_info)

            # Obtener información de usuario, filtrando por id
            usuario = Usuario.objects.filter(id=id).first()
            if not usuario:
                return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            usuario_serializer = usuarioSerializer(usuario)

            # Combinar la información en un solo diccionario
            combined_data = {
                'laboralInformation': laboral_serializer.data,
                'academicInformation': academic_serializer.data,
                'usuario': usuario_serializer.data,  # Incluye la imagen automáticamente
            }

            return Response(combined_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
class CombinedInfoApiView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            # Obtener información laboral, filtrando por id
            laboral_info = laboralInformation.objects.filter(id=id).first()
            if not laboral_info:
                return Response({'error': 'Información laboral no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            laboral_serializer = laboralInformationSerializer(laboral_info)

            # Obtener información académica, filtrando por id
            academic_info = AcademicInformation.objects.filter(id=id).first()
            if not academic_info:
                return Response({'error': 'Información académica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            academic_serializer = academicInformationSerializer(academic_info)

            # Obtener información de usuario, filtrando por id
            usuario = Usuario.objects.filter(id=id).first()
            if not usuario:
                return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            usuario_serializer = usuarioSerializer(usuario)  # Ahora se usa UsuarioSerializer

            # Combinar la información en un solo diccionario
            combined_data = {
                'laboralInformation': laboral_serializer.data,
                'academicInformation': academic_serializer.data,
                'usuario': usuario_serializer.data,
            }

            return Response(combined_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
