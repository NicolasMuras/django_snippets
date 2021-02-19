from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.api.serializers.user_serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    # Crea un nuevo usuario en el sistema.
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    # Crea un nuevo token para el usuario.
    serializer_class = AuthTokenSerializer
    # la siguiente linea nos permite visualizar el endpoint y obtener un token.
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    # El usuario necesitara estar logeado para utilizar la app,
    # para esto utilizamos 'TokenAuthentication', 
    # nos permitira adherir el 'user' a la request y utilizarlo mas adelante.
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        # Obtenemos el modelo del usuario que esta logeado.
        return self.request.user