from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    # **extra_fields nos permite tener un ModelManager mas flexible.
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('El usuario debe tener un email valido.')

        # El metodo 'normalize_email' viene de BaseUserManager,
        # nos sirve para convertir a lowercase los caracteres que vienen luego del '@'.
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # utilizamos 'set_password' una funcion de AbstracBaseUser, 
        # para poder encriptar la contraseña y evitar almacenarla en texto plano.
        user.set_password(password)

        # Es buena practica utilizar el argument 'self._db' para soportar diferentes bases de datos.
        user.save(using=self._db)

        return user

    # Nos permite crear usuarios con mas privilegios.
    def create_superuser(self, email, password):
        
        # Reutilizamos el codigo de create_user
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# PermissionsMixin nos da caracteristicas que extienden la funcionalidad del modelo usuario de Django.
class User(AbstractBaseUser, PermissionsMixin):

    # Modelo usuario soporta la utilización de email en lugar de username.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # Para crear un usuario admin necesitamos utilizar un comando especial.
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    # Sobreescribimos el valor de USERNAME_FIELD para utilizar 'email' en el lugar de 'username'.
    USERNAME_FIELD = 'email'