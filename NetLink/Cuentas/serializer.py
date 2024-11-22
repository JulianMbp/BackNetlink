from Cuentas.models import Experience, laboralInformation, AcademicInformation, Usuario
from rest_framework import serializers

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields =('id','company', 'position', 'description')

class laboralInformationSerializer(serializers.ModelSerializer):
    latestPosition = experienceSerializer()
    previousExperiences = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Experience.objects.all(), required=False  # Hacer que no sea obligatorio
    )
    
    class Meta:
        model = laboralInformation
        fields = ('id', 'latestPosition', 'abilities', 'previousExperiences', 'lookingForEmployement', 'desiredPosition', 'desiredCountry', 'telecommuting')

    def create(self, validated_data):
        latest_position_data = validated_data.pop('latestPosition')
        previous_experiences= validated_data.pop('previousExperiences', [])
        
        latest_position = Experience.objects.create(**latest_position_data)
        
        laboral_info = laboralInformation.objects.create(latestPosition=latest_position, **validated_data)
        
        laboral_info.previousExperiences.set(previous_experiences)
        laboral_info.save()
        
        return laboral_info
    
class academicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicInformation
        fields =('id', 'educativeInstitution', 'title','academicDiscipline','startDate', 'endDate','aditionalActivities', 'description','abilities')

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'contrasena', 'fechaNacimiento', 'email', 'paisOrigen', 'imagen']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # No necesitas hacer cambios si no manejas multimedia directamente
        if not instance.imagen:
            data['imagen'] = None  # Si no hay imagen, establecerla como None
        return data
