from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()
# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=255, unique=True, verbose_name="Title")
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	last_updated = models.DateTimeField(auto_now=True)
	created_on = models.DateField(blank=True, null=True)
	published = models.BooleanField(default=False, verbose_name="Published")
	content = models.TextField(blank=True, verbose_name="content")

	class Meta:
		ordering = ['-created_on']
		verbose_name = 'Post'

	def __str__(self):
		return self.title

	def save(self, *args ,**kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args ,**kwargs)

