from django.db import models

# Create your models here.

# crear usuario a partir de la clase User de Django
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agregar campos adicionales al perfil de usuario
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.user.username


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    # activo = models.BooleanField(default=True) # -- CODE - Parte III --- Campo agregado en migración posterior

    def __str__(self) -> str:
        return f"{self.nombre} ({self.camada})"
    


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

class EstudianteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.user.username


# clase final - 06 creacion del modelo avatar
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nombre
