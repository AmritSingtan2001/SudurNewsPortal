from django.db import models
from account.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import unidecode
from unidecode import unidecode
from django.template import defaultfilters


class AboutUS(models.Model):
    logo= models.ImageField(upload_to='logoimage/')
    chairman = models.CharField(max_length=150)
    ChiefEditor = models.CharField(max_length=150)
    DepartmentRegistrationNo = models.CharField(max_length=150)
    contactNo= models.CharField(max_length=15)
    email = models.EmailField()
    facebookUrl =models.URLField(null=True, blank=True)
    twitterUrl =models.URLField(null=True, blank=True)
    youtubeUrl =models.URLField(null=True, blank=True)

    class Meta:
        ordering =['-id',]



class CustomAutoSlugField(AutoSlugField):
    def create_slug(self, model_instance, add):
        slug = super().create_slug(model_instance, add)
        slug = unidecode(slug) 
        return slug
    

class MainCategorie(models.Model):
    categorie_name = models.CharField(max_length=150)
    main_ctg_slug = CustomAutoSlugField(populate_from = 'categorie_name', unique=True, default=None)
    icons= models.ImageField(upload_to='categorieIcons/')
    ordering =models.PositiveIntegerField()

    class Meta:
        ordering =['ordering',]

    
    def __str__(self):
        return self.categorie_name
    

class SubCategorie(models.Model):
    maincategorie = models.ForeignKey(MainCategorie, on_delete=models.CASCADE, related_name='categorie')
    subcategorie_name = models.CharField(max_length=150)
    subctgslug= CustomAutoSlugField(populate_from='subcategorie_name', unique=True, default=None)
    ordering =models.PositiveIntegerField()

    class Meta:
        ordering =['ordering',]
    def __str__(self):
        return self.subcategorie_name
    


    
class News(models.Model):
    categorie= models.ForeignKey(MainCategorie, on_delete=models.CASCADE, related_name='mainCtg')
    subCategorie = models.ForeignKey(SubCategorie, on_delete=models.CASCADE, related_name='subCtg', null=True, blank=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='newsimage/')
    discriptions = RichTextField()
    repoter =models.ForeignKey(User, on_delete=models.CASCADE, related_name='repoter')
    news_slug =CustomAutoSlugField(populate_from='title', unique=True, always_update=True)
    create_date = models.DateTimeField(auto_now_add=True)
    trending= models.BooleanField(default=False)
    feature = models.BooleanField(default=False)
    highlight = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id',]
        verbose_name = "News"
        verbose_name_plural = "News"

    
   

    def __str__(self):
        return self.title
    



ordering_number =(
    ('first',"First"),
    ('second',"Second"),
    ('third',"Third"),
    ('fourth',"Fourth"),
    ('fifth',"Fifth"),
    ('six',"Six")
)

pages =(
    ('home_page','Home Page'),
    ('news_details','News Detail')
)
class HorizontalAds(models.Model):
    name = models.CharField(max_length=150)
    image =models.ImageField(upload_to='horizontalads/')
    url =models.URLField(null=True, blank=True)
    positionNumber =models.CharField(max_length=150, choices=ordering_number)
    page = models.CharField(max_length=150,choices=pages, default='home_page')
    show = models.BooleanField(default=True)

    class Meta:
        ordering =['-id',]
    

    def __str__(self):
        return self.name




class VerticalAds(models.Model):
    name= models.CharField(max_length=150)
    image =models.ImageField(upload_to='verticalads/')
    url =models.URLField(null=True, blank=True)
    page = models.CharField(max_length=150,choices=pages, default='home_page')
    show = models.BooleanField(default=True)

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.name
    

class OurTeam(models.Model):
    title = models.CharField(max_length=150)
    about_our_team = RichTextField()

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=150)
    privacy_policy = RichTextField()

    class Meta:
        ordering =['-id',]
    
    def __str__(self):
        return self.title

    
class ContactUs(models.Model):
    title = models.CharField(max_length=150)
    contactus = RichTextField()
    

    class Meta:
        ordering =['-id',]
    
    def __str__(self):
        return self.title