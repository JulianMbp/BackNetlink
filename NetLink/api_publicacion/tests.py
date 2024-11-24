from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import publicacion
import json

class PublicacionTests(TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.publicacion_test = publicacion.objects.create(
            titulo='Test Título',
            descripcion='Test Descripción',
            multimedia=''
        )
        
        # URLs definidas según urls.py
        self.list_url = '/api/publicacion/publicacion_list'
        self.create_url = '/api/publicacion/publicacion_create'
        self.update_url = f'/api/publicacion/publicacion_update/{self.publicacion_test.id}'
        self.delete_url = f'/api/publicacion/publicacion_delete/{self.publicacion_test.id}'

    def test_get_publicaciones(self):
        """Test para obtener lista de publicaciones"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json()) > 0)

    def test_create_publicacion(self):
        """Test para crear una publicación"""
        data = {
            'titulo': 'Nuevo Título',
            'descripcion': 'Nueva Descripción',
            'multimedia': ''
        }
        response = self.client.post(
            self.create_url, 
            json.dumps(data),
            content_type='application/json'
        )
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])
        
        nueva_publicacion = publicacion.objects.filter(titulo='Nuevo Título').first()
        self.assertIsNotNone(nueva_publicacion)
        self.assertEqual(nueva_publicacion.descripcion, 'Nueva Descripción')

    def test_update_publicacion(self):
        """Test para actualizar una publicación"""
        data = {
            'titulo': 'Título Actualizado',
            'descripcion': 'Descripción Actualizada',
            'multimedia': ''
        }
        response = self.client.put(
            self.update_url,
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        publicacion_actualizada = publicacion.objects.get(id=self.publicacion_test.id)
        self.assertEqual(publicacion_actualizada.titulo, 'Título Actualizado')

    def test_delete_publicacion(self):
        """Test para eliminar una publicación"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            publicacion.objects.filter(id=self.publicacion_test.id).exists()
        )

    def test_get_publicacion_not_found(self):
        """Test para verificar comportamiento con ID inexistente"""
        url = '/api/publicacion/publicacion_detail/99999'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_publicacion_invalid_data(self):
        """Test para verificar validación de datos"""
        data = {
            'titulo': '',
            'descripcion': 'Test Descripción',
            'multimedia': ''
        }
        response = self.client.post(
            self.create_url,
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)