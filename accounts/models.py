from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100, default='')
    grand_father_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=15, default='')
    dob_ad = models.DateField()
    dob_bs = models.DateField()
    gender = models.CharField(max_length=100, default='0')
    provience_number = models.CharField(max_length=15, default='0')
    district = models.CharField(max_length=15, default='0')
    token = models.CharField(max_length=100, default='')

    user_image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator( ['png','jpg','jpeg'] ) ])
    # models.ImageField(default='default.jpg', upload_to='pics')
    docs_front = models.FileField(null=True, blank=True, validators=[FileExtensionValidator( ['png','jpg','jpeg'] ) ])
    # models.ImageField(default='default.jpg', upload_to='docs_front')
    docs_back = models.FileField(null=True, blank=True, validators=[FileExtensionValidator( ['png','jpg','jpeg'] ) ])
    # models.ImageField(default='default.jpg', upload_to='docs_back')

    # user_image = models.ImageField(default='default.jpg', upload_to='pics')
    # docs_front = models.ImageField(default='default.jpg', upload_to='docs_front')
    # docs_back = models.ImageField(default='default.jpg', upload_to='docs_back')


    def __str__(self):
        # return str(self.father_name)
        return '%s %s' % (self.user.first_name, self.user.username)