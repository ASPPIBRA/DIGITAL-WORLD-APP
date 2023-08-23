from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título do Post")
    summary = models.CharField(max_length=200, verbose_name="Resumo do Post")
    text = models.TextField(verbose_name="Texto do Post")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuário Criador do Post")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Imagem do Post", null=True, blank=True)
    main_post = models.BooleanField(default=False, verbose_name="Post Principal")
    date_post = models.DateTimeField(verbose_name="Data do Post", null=True, blank=True)

    def __str__(self):
        return self.title
