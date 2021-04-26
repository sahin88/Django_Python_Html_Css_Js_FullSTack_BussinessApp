from django.contrib import admin


from .models import about_model, application_model, product_model, home_model, contacts_model, contactinfo_model,newsfeed_model


class ContactInfoadmin(admin.ModelAdmin):

    list_display = ('id', 'adress',)
    list_display_links = ('id', 'adress',)
    search_fields = ('adress',)
    list_per_page = 24

class Contactadmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name','email')
    search_fields = ('description','title', 'subject','email')
    list_per_page = 24



class Aboutadmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('description','title')
    list_per_page = 24


class NewsFeedadmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('description','title')
    list_per_page = 24

class Applicationadmin(admin.ModelAdmin):

    list_display = ('id', 'application_field',)
    list_display_links = ('id', 'application_field')
    search_fields = ('description1','description2','application_field')
    list_per_page = 24


class Productadmin(admin.ModelAdmin):

    list_display = ('id', 'product_name',)
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name',)
    list_per_page = 24

class Homeadmin(admin.ModelAdmin):

    list_display = ('id', 'msg1',)
    list_display_links = ('id', 'msg1')
    search_fields = ('msg1',)
    list_per_page = 24


admin.site.register(contactinfo_model,ContactInfoadmin)

admin.site.register(newsfeed_model, NewsFeedadmin)

admin.site.register(contacts_model, Contactadmin)


admin.site.register(home_model, Homeadmin)

admin.site.register(product_model, Productadmin)

admin.site.register(application_model, Applicationadmin)

admin.site.register(about_model, Aboutadmin)
# Register your models here.
