from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
 
    published_date = models.DateTimeField(
            blank=True, null=True)
  
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):#This is to create a new model for review section
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    #This is to show which post this comment belongs to. 
    author = models.CharField(max_length=200)
    #This is to define the author of the comment.
    text = models.TextField()
    #The exact text of the comment.
    created_date = models.DateTimeField(default=timezone.now)
    #This is to show when the comment is created.
    approved_comment = models.BooleanField(default=False)
    ###A new type of field!! It allows us to have access to comments from within the Post model.
    
    def approve(self):
        self.approved_comment = True
        self.save()#save the comment if approved.

    def __str__(self):
        return self.text#to show the recently created comment.

class ProgrammingCategory(models.Model):
    Catagory = models.CharField(max_length=200)
    def __str__(self):
        return self.Catagory
#To create a new model for catagory(not completed).





# Don't forget to make migration right after modify the MODEL.
# Create your models here.
