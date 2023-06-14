from django.core.validators import RegexValidator
from django.db import models


phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 12 digits allowed.")

class User(models.Model):
    email = models.CharField(max_length=320, blank=True, null=True)
    last_name = models.CharField(max_length=254, blank=True, null=True)
    first_name = models.CharField(max_length=254, blank=True, null=True)
    additional_name = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True)

    def __str__(self):
        return f'{self.first_name}'


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()

    class Meta:
        verbose_name = "coord"
        verbose_name_plural = "coords"

    def __str__(self):
        return f'{self.latitude} - {self.longitude} - {self.height}'



class Level(models.Model):
    level = (
            ('1a','1А'),
            ('2a','2А'),
            ('3a','3А'),
            ('4a','4А')
             )
    winter = models.CharField(max_length=2, blank=True, choices=level)
    summer = models.CharField(max_length=2, blank=True, choices=level)
    autumn = models.CharField(max_length=2, blank=True, choices=level)
    spring = models.CharField(max_length=2, blank=True, choices=level)

    class Meta:
        verbose_name = "level"
        verbose_name_plural = "level"

    def __str__(self):
        return f'{self.winter} - {self.summer} - {self.autumn}- {self.spring}'


class Pereval(models.Model):
    STATUS_CHOICES = [
        ('new', 'new'),
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    beauty_title = models.TextField(blank=False)
    title = models.TextField(blank=False)
    other_titles = models.TextField(blank=False)
    connect = models.TextField(blank=False, null=True)
    add_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "pereval"
        verbose_name_plural = "pereval"


    def __str__(self):
        return f'{self.title} - {self.other_titles}'


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, related_name="images", on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    data = models.CharField(blank=True, max_length=512)

    class Meta:
        verbose_name = "picture"
        verbose_name_plural = "pictures"

    def __str__(self):
        return f"{self.title}"