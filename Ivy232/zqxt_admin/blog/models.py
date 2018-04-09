from django.db import models

# Create your models here.
 
class Article(models.Model):
    title = models.CharField('Tielw', max_length=256)
    content = models.TextField('Content')
 
    pub_date = models.DateTimeField('PublishDate', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('ApdateDate',auto_now=True, null=True)
