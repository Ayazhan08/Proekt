from django.db import models
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')



# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField(default='default value')
    author = models.CharField(max_length=30, default='anonymous')
    # email = models.EmailField(blank=True)
    describe = models.TextField(default='DataFlair Django tutorials')

    def __str__(self):
        return self.title




    class Meta:
        verbose_name = "Мақала"
        verbose_name_plural = "Мақалалар"
        ordering = ['-author', 'title']





class Categories(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    picture=models.ImageField(default='default value')
    describe=models.TextField(default='DataFlair Django tutorials')


    def is_equal(self):
        l=100
        if l == 100:
            return 1


class Labs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Takyryp")
    is_published = models.BooleanField(default=True, verbose_name="Wyggarylym")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.id})


class Mids(models.Model):
    title = models.CharField(max_length=255, verbose_name="Takyryp")
    is_published = models.BooleanField(default=True, verbose_name="Wyggarylym")
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})


class Registration(models.Model):
    Name = models.CharField(max_length=15)
    Lastname = models.CharField(max_length=30, verbose_name="First name", validators=[alphanumeric])
    Username = models.CharField(max_length=15)
    NameDad = models.CharField(max_length=15)
    Email  = models.EmailField(blank=True, unique=True)
    PhoneNumber = models.IntegerField(max_length=11, unique=True)
    Password = models.CharField(max_length=10)



    def str(self):
        return self.name


