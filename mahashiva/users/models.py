import  django

# Create your models here.


from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
#
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "title:{}, author:{}, email:{} ,date: {}".format(self.title,self.author,self.email,self.date)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)



    def __str__(self):
        return "title:{}, code:{}, langage:{} ,created: {}".format(self.title,self.code,self.language,self.created)

    class Meta:
        ordering = ['created']







class Image(models.Model):
   image=models.ImageField(upload_to='upload_image', null=True)

   def __str__(self):
       return 'id: {} image: {}'.format(self.id,self.image)
