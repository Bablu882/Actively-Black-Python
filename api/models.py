from django.db import models

from management.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Student(models.Model):
    owner=models.ForeignKey(User,related_name='students',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    highlighted=models.TextField()


    def save(self,*args,**kwargs):
        lexer=get_lexer_by_name(self.language)
        linenos='table' if self.linenos else False
        options={'title':self.title} if self.title else {}
        formatter=HtmlFormatter(style=self.style,linenos=linenos,full=True,**options)
        self.highlighted=highlight(self.code,lexer,formatter)
        super().save(*args,**kwargs)
