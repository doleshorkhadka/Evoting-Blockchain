from django.db import models

class Election(models.Model):
    status = models.BooleanField(default=False)
    
    def __bool__(self):
        return self.status
