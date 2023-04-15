from django.db import models as db_models

# Create your models here.
class Post(db_models.Model):
    username = db_models.CharField(max_length=12, null=False, blank=False)
    title = db_models.CharField(max_length=50,  null=True, blank=True)
    content = db_models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
