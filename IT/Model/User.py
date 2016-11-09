<<<<<<< HEAD
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
=======
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
>>>>>>> b6ed3cb0427fc3b30fe2f4b569908246cfec5690
    last_name = models.CharField(max_length=30)