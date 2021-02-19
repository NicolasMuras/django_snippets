from django.contrib.auth import get_user_model, authenticate
# se puede pasar los mensajes que lanzaremos en pantalla por la funcion: ugettext_lazy
# de esta manera tendremos soporte para traducir dichos mensajes.
# el objeto real se convierte en 'string' a ultimo momento
# para saber que idioma utiliza el navegador y asi traducirlo.
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        # Crear usuario con contraseña encriptada y devolverlo.
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        # Ejecutamos 'update' en el resto de 'validated_date' dejando afuera a 'password'
        # Super llamara a la función 'update' original.
        user = super().update(instance, validated_data)

        # Setteamos la password.
        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    
    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace = False
        )

    def validate(self, attrs):
        # Validamos y autenticamos al usuario utilizando la funcion 'authenticate'.

        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password,
        )

        if not user:
            msg = _('Credenciales incorrectas.')
            raise serializers.ValidationError(msg, code = 'authentication')

        attrs['user'] = user
        return attrs