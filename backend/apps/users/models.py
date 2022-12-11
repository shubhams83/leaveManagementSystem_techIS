from django.db import models

# Create your models here.


class User(models.Model):
    class meta(object):
        db_table = 'user'