from django.db import models

# Create your models here.
class Post(models.Model):
	message = models.TextField()
	is_public = models.BooleanField(default=False, verbose_name='공개여부')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.message

	# def message_length(self):
	# 	return len(self.message)
	# message_length.short_description = "메세지 글자수"