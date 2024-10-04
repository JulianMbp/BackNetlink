from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Experience(models.Model):
    company = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    def getCompany(self):
        return self.company
    def setCompany(self, company):
        self.company = company
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description

class laboralInformation(models.Model):
    latestPosition = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name='+')
    abilities = ArrayField(models.CharField(max_length=100), blank=True)
    previousExperiences = models.ManyToManyField(Experience)
    lookingForEmployement = models.BooleanField()
    desiredPosition = models.CharField(max_length=20)
    desiredCountry = models.CharField(max_length=20)
    telecommuting = models.BooleanField()
    def getLatestPosition(self):
        return self.latestPosition
    
    def setLatestPosition(self, company, position, description):
        self.latestPosition = Experience(company, position, description)
    
    def getAbilities(self):
        return self.abilities
    
    def setAbilities(self, ability):
        self.abilities.append(ability)
    
    def getPreviousExperiences(self):
        return self.previousExperiences
    
    def setPreviousExperiences(self, company, position, description):
        newExperience = Experience(company, position, description)
        self.previousExperiences.append(newExperience)
    
    def getLookingForEmployement(self):
        return self.lookingForEmployement
    
    def setLookingForEmployement(self, isLooking):
        self.lookingForEmployement = isLooking
    
    def getDesiredPosition(self):
        return self.desiredPosition
    
    def setDesiredPosition(self, desiredPosition):
        self.desiredPosition = desiredPosition
    
    def getDesiredCountry(self):
        return self.desiredCountry
    
    def setDesiredCountry(self, desiredCountry):
        self.desiredCountry = desiredCountry
    
    def getTelecommuting(self):
        return self.telecommuting
    
    def setTelecommuting(self, telecommuting):
        self.telecommuting = telecommuting
    
    def addExperience(self, company, position, description):
        newExperience = Experience(company, position, description)
        self.previousExperiences.add(newExperience)
        return self.previousExperiences
    
    def addAbility(self, ability):
        self.abilities.append(ability)
        return self.abilities
        