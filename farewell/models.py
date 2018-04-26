from django.db import models


class query(models.Model):
    name = models.CharField(max_length=50, default='NA')
    email = models.EmailField(default='NA')
    text = models.TextField(max_length=1000, default='NA')

    def __str__(self):
        return(self.name+' | '+self.course+' | '+self.email+' | '+self.text)
    
