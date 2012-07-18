from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField()

    def __unicode__(self):
        return self.nome

TIPOS_FONE = (
        ('cel','celular'),
        ('com','comercial'),
        ('res','residencial'),
        ('rec','recados'),
    )

class Fone(models.Model):
    contato = models.ForeignKey(Contato)
    tipo = models.CharField(max_length=8, choices= TIPOS_FONE)
    ddd = models.CharField(max_length=8, default='5511')
    numero = models.CharField(max_length=16)

    def __unicode__(self):
        return '(%s) %s' % (self.ddd, self.numero)
