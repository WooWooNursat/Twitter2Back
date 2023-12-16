from django.db import models
from authorization.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    dateOfCreation = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.title + ' ' + str(self.author)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
