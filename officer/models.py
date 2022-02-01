from django.db import models
# Create your models here.

class Election(models.Model):
    status = models.BooleanField(default=False)
    user_sts = models.BooleanField(default=False)
    
    
    def __bool__(self):
        return self.status
    