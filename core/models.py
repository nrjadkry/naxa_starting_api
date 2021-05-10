from django.db import models

from django.db.models.signals import pre_save, post_save


#  Custom Model Manager
class StudentManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().order_by('first_name')

	def get_student_range(self, r1, r2):
		return super().get_queryset().filter(roll__range=(r1,r2))

class Student(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	full_name= models.CharField(blank=True,null=True,max_length=200)
	address=models.CharField(max_length=100)
	roll=models.IntegerField()
	email=models.CharField(max_length=100)

	objects=StudentManager()


	def __str__(self):
		return self.first_name


	# Customize save method
	def save(self, *args, **kwargs):
		self.full_name = str(self.first_name) + ' ' + str(self.last_name)
		print('Student saved')
		super().save(*args,**kwargs)

# Post save method
def post_student_save(sender,instance,**kwargs):
	print('Student post saved')

post_save.connect(post_student_save, Student)

# Pre save method
def pre_student_save(sender, instance, **kwargs):
	print('Student pre save')

pre_save.connect(pre_student_save, Student)




# first name and last name 
# method in model manager full name by concat first name and last name
# customize save method in django model
# post_save and pre_save signals


