from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename



class Base(models.Model):
    criado = models.DateField('Criado em', auto_now_add=True)
    modificado = models.DateField('Modificado em', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta():
        abstract = True

class Project(Base):
    name = models.CharField('Projeto', max_length=100)
    language = models.CharField('Language', max_length=100)
    deploy = models.URLField('Deploy',max_length=100, blank=True)
    git = models.URLField('Git', max_length=100, blank=True)
    image = StdImageField('Image', upload_to=get_file_path, variations= {'thumb': {'width' : 480, 'height': 480, 'crop': True}})


    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name