from django.db import models

class Usuario(models.Model):
    
    usuario_apelido = models.CharField(primary_key=True, max_length=100, default='')
    usuario_nome = models.CharField(max_length=150, default='')
    usuario_email = models.EmailField(default='')
    usuario_idade = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Nome de Usuário: {self.usuario_apelido} | E-mail: {self.usuario_email}'

class UsuarioTask(models.Model):
    usuario_apelido = models.CharField(max_length=100, default='')
    usuario_task = models.CharField(max_length=255, default='')
    