from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, 
                                related_name='profile',
                                on_delete=models.CASCADE)

	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(upload_to='profile_pic', 
                                    null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True,
                                        null=True)

	def __str__(self):
		return self.name


class Todo_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                         related_name='todolist', null=True)
    name = models.CharField(max_length = 64)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    CHOICES =   (('Pending','Pending'),
                ('Done', 'Done')
    )
    name = models.CharField(max_length = 128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    todo_list = models.ForeignKey(Todo_list, on_delete=models.CASCADE , null=True)
    status = models.CharField(max_length = 64, null = True, choices = CHOICES, default='Pending')

    def __str__(self):
        return self.name