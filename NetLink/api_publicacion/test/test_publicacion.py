import json
from django.test import TestCase
from django.urls import reverse
from api_publicacion.models import Publicacion

class test_publicacion(TestCase):
    @classmethod
    def setUpTestData(cls):
        Publicacion.objects.create(
            titulo='Test Título', 
            descripcion='Test Descripción',
            multimedia='',
            )
    def tearDown(self):
        pass
class test_publicacion_list(test_publicacion):
    def test_view_publicacion_list(self):
        response=self.client.get(reverse('publicacion_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(len(response.data),1)
    def test_create_publicacion(self):
        response=self.client.post(reverse('publicacion_list'),{
            'titulo':'Test Título',
            'descripcion':'Test Descripción',
            'multimedia':'',
        })
        self.assertEqual(response.status_code,[200,201])
        filtered_publicacion=Publicacion.objects.filter(titulo='Test Título').first()
        self.assertEqual(filtered_publicacion.descripcion,'Test Descripción')
    def test_update_publicacion(self):
        mi_publicacion=Publicacion.objects.create(
            titulo='Test Título',
            descripcion='Test Descripción',
            multimedia='',
        )
        valid_publicacion={
            'titulo':'Título',
            'descripcion':'Descripción',
            'multimedia':'',
        }
        url=reverse('actualizar_publicacion',kwargs={'pkid':mi_publicacion.id})
        valid_publicacion_json=json.dumps(valid_publicacion)
        response=self.client.put(url,valid_publicacion_json,content_type='application/json')
        self.assertEqual(response.status_code,[200,201])
    def test_delete_publicacion(self):
        mi_publicacion=Publicacion.objects.create(
            titulo='Test Título',
            descripcion='Test Descripción',
            multimedia='',
        )
        url=reverse('eliminar_publicacion',kwargs={'pkid':mi_publicacion.id})
        response=self.client.delete(url)
        self.assertEqual(response.status_code,204)
        self.assertFalse(Publicacion.objects.filter(titulo='Test Título').exists())
