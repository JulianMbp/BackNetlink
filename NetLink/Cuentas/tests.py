import json
from django.test import TestCase
from django.urls import reverse
from Cuentas.models import *

class test_cuentas(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        experience = Experience.objects.create(
            company="a company",
            position="a position",
            description="a description"
        )
        labinfodata = [experience]
        labInfo=laboralInformation.objects.create(
            latestPosition=experience,
            abilities=['An Ability'],
            lookingForEmployement=True,
            desiredPosition="A good position",
            desiredCountry="A country",
            telecommuting=True
        )
        labInfo.previousExperiences.set(labinfodata)
        
    def tearDown(self):
        pass
    
    def test_view_laboral_list(self):
        response=self.client.get('/api/Netlink/Llist')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)
    
    def test_create_laboral(self):
        response = self.client.post(
            '/api/Netlink/laboralInfoAdd',
            data={
                "latestPosition":{
                        "company":"hey company",
                        "position":"hey position",
                        "description":"hey description"
                    },
                "abilities":['hey Ability'],
                "previousExperiences":[{
                        "company":"hey company",
                        "position":"hey position",
                        "description":"hey description"
                    }],
                "lookingForEmployement":True,
                "desiredPosition":"A great position",
                "desiredCountry":"un country",
                "telecommuting":True
            }
        )
        self.assertIn(response.status_code, (200, 201))
        filtered_laboral=laboralInformation.objects.filter(desiredPosition='A great position').first()
        self.assertEqual(filtered_laboral.desiredCountry, 'un country')