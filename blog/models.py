from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=66)
	objects = models.Manager()

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=25)
	objects = models.Manager()

	def __str__(self):
		return self.name


class Aritcle(models.Model):
	title = models.CharField(max_length=100)
	# 副标题
	subtitle = models.CharField(max_length=100)
	publish_data = models.DateTimeField()
	content = models.TextField()
	link = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	# 关联其他模型
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag, blank=True)
	# 防止报错
	objects = models.Manager()

	def __str__(self):
		return self.title



