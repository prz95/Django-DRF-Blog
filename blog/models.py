from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    """
    this is a class to define posts for blog app
    """

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey("category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    apdated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
