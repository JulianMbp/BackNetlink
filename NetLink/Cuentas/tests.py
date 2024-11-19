import json
from django.test import TestCase
from django.urls import reverse
from Cuentas.models import *

class test_cuentasl(TestCase):
    
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
                        "company": "A Company",
                        "position": "A position",
                        "description": "It's a very important position"
                    },
                "abilities":["Ability"],
                "previousExperiences":[{
                        "company": "A Company",
                        "position": "A position",
                        "description": "It's a very important position"
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

class test_cuentasA(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        academicInfo=AcademicInformation.objects.create(
            educativeInstitution='An institution',
            title='a title',
            academicDiscipline='an academic disc',
            startDate="2024-11-01",
            endDate="2024-11-01",
            aditionalActivities=['An activity'],
            description ='A description',
            abilities=['An Ability'],
        )
        
    def tearDown(self):
        pass
    
    def test_view_academic_list(self):
        response=self.client.get('/api/Netlink/academicList')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)
    
    def test_create_academic(self):
        response = self.client.post(
            '/api/Netlink/academicInfoAdd',
            data={
                "educativeInstitution":"Another insti",
                "title":"another title",
                "academicDiscipline":"another disc",
                "startDate":"2024-11-01",
                "endDate":"2024-11-01",
                "aditionalActivities":["Another one"],
                "description" :"Another desc",
                "abilities":["Another one"]
            }
        )
        self.assertIn(response.status_code, (200, 201))
        filtered_academic=AcademicInformation.objects.filter(educativeInstitution='Another insti').first()
        self.assertEqual(filtered_academic.title, 'another title')