from django.db import models
# from ..mahashiva.settings import AUTH_USER_MODEL
from django.conf import settings

# Create your models here.

def upload_location(instance,filename,**kwargs):
    file_path='blog/{}/{}-{}'.format(instance.author.id,instance.title,filename)
    return file_path


class Blog_Post(models.Model) :
    title=models.CharField(max_length=50,null=False,blank=False)
    body=models.TextField(max_length=5000,null=False,blank=False)
    #image=models.ImageField(upload_to=upload_location,null=False,blank=False)
    date_publish=models.DateTimeField(auto_now=True,verbose_name="date publish")
    date_updated=models.DateTimeField(auto_now=True,verbose_name="date updated")
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # slug=models.SlugField(blank=True,unique=True)
    def __str__(self):
        return 'title:{},body:{},date_publish:{},date_updated:{},author:{}'.format(self.title,self.body,self.date_publish,self.date_updated,self.author)


