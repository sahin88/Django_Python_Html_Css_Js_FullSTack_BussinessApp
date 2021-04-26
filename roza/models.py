from django.db import models
from django.utils import timezone

class home_model(models.Model):
    
    image1 = models.ImageField(
        upload_to='home/images', blank=True)

    msg1=models.CharField(max_length=255,blank=True)

    image2 = models.ImageField(
        upload_to='home/images', blank=True)
    msg2=models.CharField(max_length=255,blank=True)
    image3 = models.ImageField(
        upload_to='home/images', blank=True)
    msg3=models.CharField(max_length=255,blank=True)
    

    def __str__(self):
        return self.msg1


    def delete(self, *args, **kwargs):
        self.image.delete()
      
        super(About, self).delete(*args, **kwargs)





class about_model(models.Model):
    
    image = models.ImageField(
        upload_to='about/images', blank=True)

    title=models.CharField(max_length=255,blank=True)
    description= models.TextField(blank=True)
    #slug= models.SlugField(unique=True)

    def __str__(self):
        return self.title


    def delete(self, *args, **kwargs):
        self.image.delete()
      
        super(About, self).delete(*args, **kwargs)


 
class application_model(models.Model):
    application_field=models.CharField(max_length=255,blank=True)
    title1=models.CharField(max_length=255,blank=True)
    main1 = models.ImageField(
        upload_to='about/application/images', blank=True, null=True)
    description1= models.TextField(blank=True)
    title2=models.CharField(max_length=255,blank=True)
    main2 = models.ImageField(
        upload_to='about/application/images', blank=True, null=True)
    description2= models.TextField(blank=True, null=True)
    title3=models.CharField(max_length=255,blank=True)
    main3 = models.ImageField(
        upload_to='about/application/images', blank=True, null=True)
    description3= models.TextField(blank=True)



    def __str__(self):
        return self.application_field


class product_model(models.Model):
    product_name=models.CharField(max_length=255,blank=True)
    product_image = models.ImageField(upload_to='product/images', blank=True, null=True)
    weight_unit=models.CharField(max_length=50,blank=True)
    weight_value=models.CharField(max_length=50,blank=True)
    weft_yarn_unit=models.CharField(max_length=50,blank=True)
    weft_yarn_value=models.CharField(max_length=50,blank=True)
    warp_yarn_unit=models.CharField(max_length=50,blank=True)
    warp_yarn_value=models.CharField(max_length=50,blank=True)
    patern_unit=models.CharField(max_length=50,blank=True)
    patern_value=models.CharField(max_length=50,blank=True)
    md_tensile_strength_unit=models.CharField(max_length=50,blank=True)
    md_tensile_strength_value=models.CharField(max_length=50,blank=True)
    cd_tensile_strength_unit=models.CharField(max_length=50,blank=True)
    cd_tensile_strength_value=models.CharField(max_length=50,blank=True)
    elongation_at_break_unit=models.CharField(max_length=50,blank=True)
    elongation_at_break_value=models.CharField(max_length=50,blank=True)
    coathing_unit=models.CharField(max_length=50,blank=True)
    coathing_value=models.CharField(max_length=50,blank=True)
    core_size_unit=models.CharField(max_length=50,blank=True)
    core_size_value=models.CharField(max_length=50,blank=True)
    role_width_unit=models.CharField(max_length=50,blank=True)
    role_width_value=models.CharField(max_length=50,blank=True)
    role_length_unit=models.CharField(max_length=50,blank=True)
    role_length_value=models.CharField(max_length=50,blank=True)
    yarns_type=models.CharField(max_length=50,blank=True)
    constructions=models.CharField(max_length=50,blank=True)
    patterns=models.CharField(max_length=50,blank=True)
    bondings=models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.product_name







class contacts_model(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField( max_length=255,blank=False)
    subject = models.CharField(max_length=255)
    phone_nr = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)



    def __str__(self):
        return self.name

class contactinfo_model(models.Model):
    adress = models.CharField(max_length=250)
    email = models.CharField(max_length=255)
    working_hour = models.CharField(max_length=255)
    phone_nr = models.CharField(max_length=255)




    def __str__(self):
        return self.adress

class newsfeed_model(models.Model):
    
    image1 = models.ImageField(
        upload_to='home/bottom/images', blank=True, null=True)

    title=models.CharField(max_length=255,blank=True)
    description= models.TextField(blank=True)
    #slug= models.SlugField(unique=True)

    def __str__(self):
        return self.title

