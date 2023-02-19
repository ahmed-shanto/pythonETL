from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Company_Details(models.Model):
    name    = models.CharField(max_length=50,blank=True, null=True)
    title   = models.CharField(max_length=1000,blank=True, null=True)
    logo    = models.ImageField(upload_to="static/modules/",blank=True, null=True)
    banner1 = models.ImageField(upload_to="static/modules/",blank=True, null=True)
    banner2 = models.ImageField(upload_to="static/modules/",blank=True, null=True)
    address =models.TextField(max_length=1000,blank=True, null=True)
    email   =models.CharField(max_length=50,blank=True, null=True)
    phone   =models.CharField(max_length=20,blank=True, null=True)
    about_image_one= models.ImageField(upload_to="static/modules/",blank=True, null=True)
    about_image_two= models.ImageField(upload_to="static/modules/",blank=True, null=True)
    about_image_three= models.ImageField(upload_to="static/modules/",blank=True, null=True)
    about_image_four= models.ImageField(upload_to="static/modules/",blank=True, null=True)
    about_title= models.CharField(max_length=50,blank=True, null=True)
    about_short_desc= models.TextField(max_length=1000,blank=True, null=True)
    about_leader_name= models.CharField(max_length=50,blank=True, null=True)
    about_leader_designation= models.CharField(max_length=50,blank=True, null=True)
    about_leader_speech= models.TextField(max_length=1000,blank=True, null=True)
    about_leader_image= models.ImageField(upload_to="static/modules/",blank=True, null=True)
    about_userarea_image1=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    about_userarea_image2=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Company_Details"
        verbose_name_plural = "Company_Details"

    def __str__(self) :
        return str('Company_Details')

    def convert_to_list(self):
        first_line = self.address.split(" ")[0:4]
        second_line = self.address.split(" ")[4:8]
        third_line= self.address.split(" ")[8:11]
        fourth_line=self.address.split(" ")[11::]

        return " ".join(first_line)," ".join(second_line)," ".join(third_line)," ".join(fourth_line)

class About_Count(models.Model):
    title=models.CharField(max_length=500,blank=True, null=True)
    number=models.CharField(max_length=50,blank=True, null=True)
    icon=models.CharField(max_length=50,blank=True, null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)
    



    class Meta:
        verbose_name = "About_Count"
        verbose_name_plural = "About_Count"

    def __str__(self) :
        return self.title

        
class Static_Files(models.Model):
    home_features_title1=models.CharField(max_length=1000,blank=True, null=True)
    home_features_title2=models.CharField(max_length=1000,blank=True, null=True)
    home_products_heading=models.CharField(max_length=1000,blank=True, null=True)
    home_products_title=models.TextField(max_length=1000,blank=True, null=True)
    service_QA_title=models.CharField(max_length=1000,blank=True, null=True)
    service_QA_image=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    product_QA_desc=models.TextField(max_length=1000,blank=True, null=True)

    
    class Meta:
        verbose_name="Static_Files"
        verbose_name_plural="Static_Files"

    def __str__(self):
        return str('Static_Files')

    def convert_to_list(self):
        first_line = self.home_products_title.split(" ")[0:4]
        second_line = self.home_products_title.split(" ")[4::]
        return " ".join(first_line)," ".join(second_line)

class Home_Features(models.Model):
    title=models.CharField(max_length=1000,blank=True,null=True)
    name       =models.TextField(max_length=1000,blank=True,null=True)
    short_desc =RichTextField(blank=True, null=True)
    image       =models.ImageField(upload_to="static/modules/",blank=True, null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Home_Features"
        verbose_name_plural = "Home_Features"

    def __str__(self) :
        return self.title


class Exclusive_Features(models.Model):
    name       =models.CharField(max_length=1000,blank=True,null=True)
    short_desc =models.TextField(max_length=1000,blank=True,null=True)
    icon       =models.ImageField(upload_to="static/modules/",blank=True, null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Exclusive_Features"
        verbose_name_plural = "Exclusive_Features"

    def __str__(self) :
        return self.name

class Home_Products(models.Model):
    name       =models.CharField(max_length=1000,blank=True,null=True)
    short_desc =models.TextField(max_length=2000,blank=True,null=True)
    icon       =models.ImageField(upload_to="static/modules/",blank=True, null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Home_Products"
        verbose_name_plural = "Home_Products"

    def __str__(self) :
        return self.name

class Clients(models.Model):
    name       =models.CharField(max_length=100,blank=True,null=True)
    icon       =models.ImageField(upload_to="static/modules/",blank=True, null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"
        
    def __str__(self) :
        return str(self.name)

class Events(models.Model):
    title       =models.CharField(max_length=1000,blank=True,null=True)
    image       =models.ImageField(upload_to="static/modules/",blank=True, null=True)
    link       =models.CharField(max_length=1000,blank=True,null=True)
    date       =models.CharField(max_length=100,blank=True,null=True)
    short_desc =RichTextField(blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"

    def __str__(self) :
        return str('Events')



class Services(models.Model):
    name       =models.CharField(max_length=100,blank=True,null=True)
    description =RichTextField(blank=True,null=True)
    icon = models.CharField(max_length=50,blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"

    def __str__(self) :
        return self.name

class Product(models.Model):
    name       =models.CharField(max_length=100,blank=True,null=True)
    title=models.CharField(max_length=1000,blank=True,null=True)
    website_link=models.CharField(max_length=500,blank=True,null=True)
    image   =models.ImageField(upload_to="static/modules/",blank=True, null=True)
    description= models.TextField(max_length=1000,blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"

    def __str__(self) :
        return self.name

class Product_Name(models.Model):
    name_with_title    =models.CharField(max_length=1000,blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)


    

    class Meta:
        verbose_name = "Product_Name"
        verbose_name_plural = "Product_Name"

    def __str__(self) :
        return self.name_with_title


class Modules(models.Model):
    product_name     = models.ForeignKey(Product_Name, on_delete=models.CASCADE, related_name='modules')
    name        = models.CharField(max_length=50,blank=True, null=True)
    title= models.CharField(max_length=1000,blank=True, null=True)
    bg_image=models.ImageField(upload_to="static/modules/",blank=True, null=True)
    photo_one      = models.ImageField(upload_to="static/modules/", blank=True, null=True)
    benifits_one= models.CharField(max_length=1000,blank=True, null=True)
    benifits_two= models.CharField(max_length=1000,blank=True, null=True)
    benifits_three= models.CharField(max_length=1000,blank=True, null=True)
    benifits_four= models.CharField(max_length=1000,blank=True, null=True)
    benifits_five= models.CharField(max_length=1000,blank=True, null=True)
    benifits_six= models.CharField(max_length=1000,blank=True, null=True)
    benifits_seven= models.CharField(max_length=1000,blank=True, null=True)
    benifits_eight= models.CharField(max_length=1000,blank=True, null=True)
    photo_two     = models.ImageField(upload_to="static/modules/", blank=True, null=True)
    description_two= RichTextField(blank=True, null=True)
    ordering    = models.IntegerField(default=1)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self) :
        return self.name



class Vacancy(models.Model):
    name       =models.CharField(max_length=100,blank=True,null=True)
    place      = models.CharField(max_length=500,blank=True,null=True)
    salary      = models.CharField(max_length=500,blank=True,null=True)
    date      = models.CharField(max_length=500,blank=True,null=True)
    type      = models.CharField(max_length=500,blank=True,null=True)
    experience      = models.CharField(max_length=500,blank=True,null=True)
    description = RichTextField(blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancy"

    def __str__(self) :
        return self.name

class ApplyJob(models.Model):
    linked_jobs     = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applyjob',blank=True,null=True)
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=100)
    phone    = models.CharField(max_length=13)
    resume   = models.FileField(upload_to="static/resumes/")
    date= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Cantidate Details"
        verbose_name_plural = "Cantidate Details"

    def __str__(self) :
        return str('Resume Of '+ self.name)

class Product_QA(models.Model):
    question       =models.TextField(max_length=2000,blank=True,null=True)
    answer      = models.TextField(max_length=2000,blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = "Product_QA"
        verbose_name_plural = "Product_QA"

    def __str__(self) :
        return self.question

class Service_QA(models.Model):
    question       =models.TextField(max_length=2000,blank=True,null=True)
    answer      = models.TextField(max_length=2000,blank=True,null=True)
    ordering   = models.IntegerField(default=1)
    status     = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = "Service_QA"
        verbose_name_plural = "Service_QA"

    def __str__(self) :
        return self.question


class Contact(models.Model):
    module     = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='module',blank=True,null=True)
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=100)
    phone    = models.CharField(max_length=13)
    message  =models.TextField(max_length=1000)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str('Message From '+ self.name)
