from django.db import models

# Create your models here.
class CodeSnippet(models.Model):
  language = models.CharField(max_length=50)
  code = models.TextField()
  result = models.TextField(null= True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)