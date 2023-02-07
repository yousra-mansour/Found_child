from django.db import models

class found_child_data(models.Model):
    person_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    phone_number = models.CharField( max_length=12) 
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null = True)
    img = models.ImageField(upload_to='found_photos')


    def __str__(self):
        return self.child_name


class missing_child_data(models.Model):
    person_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    phone_number = models.CharField( max_length=12) 
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null = True)
    img = models.ImageField(upload_to='missing_photos')


    def __str__(self):
        return self.child_name
