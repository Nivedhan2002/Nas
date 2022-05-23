from django.db import models
from django import forms

# Create your models here.

class uploadForm(models.Model):
    name = models.CharField(max_length = 30)
    img = models.ImageField(blank = True, null = True)
    doc = models.FileField(blank = True, null = True)
    def __str__(self):
        return f'{self.name}'
    # def upload_image(self, filename):
    #     return 'uploadForm/{}/{}'.format(self.title, filename)

class uploadMForm(forms.ModelForm):
    class Meta():
        model = uploadForm
        fields = ['name', 'img', 'doc']