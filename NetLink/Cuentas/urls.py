from django.urls import path
from .views import laboralInformationApiView, academicInformationApiView, experienceApiView, UsuariosView, UsuarioQueryApiView, validateApiView, CombinedInfoApiView

urlpatterns=[
    path('login', validateApiView.as_view()),

    path('Llist', laboralInformationApiView.as_view()),
    path('getLinfo/<int:pkid>', laboralInformationApiView.as_view()),
    path('laboralInfoAdd', laboralInformationApiView.as_view()),
    
    path('getAll', experienceApiView.as_view()),
    path('getExperience', experienceApiView.as_view()),
    path('addExperience', experienceApiView.as_view()),
    path('updateExperience/<int:pkid>', experienceApiView.as_view()),
    path('deleteExperience/<int:pkid>', experienceApiView.as_view()),
    
    path('academicList', academicInformationApiView.as_view()),
    path('getAcademicInfo/<int:pkid>', academicInformationApiView.as_view()),
    path('academicInfoAdd', academicInformationApiView.as_view()),
    path('academicInfoUpdate/<int:pkid>', academicInformationApiView.as_view()),

    path('list', UsuariosView.as_view()),
    path('crear-usuario', UsuariosView.as_view()),
    path ('actualizar-usuario/<int:pkid>', UsuariosView.as_view(), name="actulizar_usuario"),
    path ('eliminar-usuario/<int:pkid>', UsuariosView.as_view(), name="eliminar_usuario"),
    path ('consultar/<int:pkid>', UsuarioQueryApiView.as_view(), name ="consultar"),

    path('combined-info/<int:id>/', CombinedInfoApiView.as_view(), name='combined-info')

]