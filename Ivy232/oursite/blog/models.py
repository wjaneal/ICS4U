from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
# this line defines our model (it is an object). # Post is the name of our model
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.

	# Properties / type of each field
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # a link to another model
    title = models.CharField(max_length=200) # text with a limited number of characters
    text = models.TextField() # long text without a limit
    created_date = models.DateTimeField(
            default=timezone.now) # date and time
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.CharField(max_length=20,default="")
        # Method
    def publish(self): 
        self.published_date = timezone.now()
        self.save()

    def __str__(self): 
# two underscore characters (_) on each side of str
        return self.title

