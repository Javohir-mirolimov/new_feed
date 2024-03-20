from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from .validators import ImageFileValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam', null=True, blank=True, validators=[
        RegexValidator(
            regex= r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])


    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    description = models.CharField(max_length=25)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Turi'
        verbose_name_plural = 'Turlari'


    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    desciption = models.CharField(max_length=55)
    news = models.ManyToManyField(to='NewsItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Pasts'

class Image(models.Model):
    img = models.ImageField(validators=[(ImageFileValidator)],  verbose_name='rasm', upload_to='photo_new/')
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='ismi')
    email = models.CharField(max_length=255, verbose_name='email')
    message = models.TextField(verbose_name='xabar')

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'

class Info(models.Model):
    img = models.ImageField(validators=[(ImageFileValidator)],  verbose_name='rasm', upload_to='photo/')
    sponsor_img = models.ImageField(validators=[(ImageFileValidator)],  verbose_name='xomiy_rasmi', upload_to='photo_sponsor/')
    video = models.URLField()
    facebook = models.CharField(max_length=35)
    twitter = models.CharField(max_length=35)
    youtube = models.CharField(max_length=35)
    email = models.EmailField(validators=[(EmailValidator)], verbose_name='elektiron manzil')

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Info'

