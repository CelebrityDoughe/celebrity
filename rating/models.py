from django.db import models


class Celebrity(models.Model):
    """
    Celebrity Model
    """
    CELEBRITY_CHOICES = (('A','Actors'),
                         ('M','Musicians'),
                         ('T','TV'),
                         ('R','Radio'),
                         ('S','Sports'),
                         ('P','Politicians'))

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    specificity = models.CharField(max_length=1, choices=CELEBRITY_CHOICES)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to="images/celebritypics")

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    """
    Contact Page Model
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    detail = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s(%s) - %s" % (self.name, self.email, self.dt_created)

