from django.db import models
from apps.users.models import User
from config.constants import LEAVE_TYPE

# Create your models here.
class Leave(models.Model):
    class meta(object):
        db_table = 'leave'


    employee_id = models.ForeignKey(User, blank=False, null= False, db_index=True)
    user_name = models.ForeignKey(User, blank=False, null=False, db_index=True)
    leave_type = models.CharField('Leave Type', blank=False, null=False, default='N/A', choices=LEAVE_TYPE, max_length=50)
    from_date = models.DateTimeField('From Date', blank=False, null=False)
    to_date = models.DateTimeField('To Date', blank=False, null=False)
    duration = models.IntegerField('Duration', blank=False, null=False,default=0)
    created_at = models.DateTimeField('Created Datetime', blank=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated Datetime', blank=False, auto_now=True)

    def __str__(self):
        return self.name

