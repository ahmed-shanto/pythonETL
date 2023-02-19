from django.contrib import admin
from .models import * 

# Register your models here.

mymodels = [Company_Details,Static_Files]
admin.site.register(mymodels)


class About_CountAdmin(admin.ModelAdmin):
    list_display = ["title",'number', 'icon','ordering','status']
    list_filter = ['title','number','status','ordering']
    search_fields=['title','number']

admin.site.register(About_Count,About_CountAdmin)

class Home_FeaturesAdmin(admin.ModelAdmin):
    list_display = ["title",'name', 'short_desc','image','ordering','status']
    list_filter = ['title','status','ordering']
    search_fields=['title','name','short_desc']

admin.site.register(Home_Features,Home_FeaturesAdmin)

class Exclusive_FeaturesAdmin(admin.ModelAdmin):
    list_display = ["name", 'short_desc','icon','ordering','status']
    list_filter = ['status','ordering']
    search_fields=['name','short_desc']

admin.site.register(Exclusive_Features,Exclusive_FeaturesAdmin)

class Home_ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_desc','icon','ordering','status']
    list_filter = ['name','status','ordering']
    search_fields=['name','short_desc']

admin.site.register(Home_Products,Home_ProductsAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name','icon','ordering','status']
    list_filter = ['status','ordering']
    search_fields=['name']

admin.site.register(Clients,ClientsAdmin)

class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image','link','date','short_desc','ordering','status']
    list_filter = ['title','status','ordering']
    search_fields=['title','link','short_desc','date']

admin.site.register(Events,EventsAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','icon','ordering','status']
    list_filter = ['name','status','ordering']
    search_fields=['name','description','icon']

admin.site.register(Services,ServicesAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'title','website_link','description','ordering','status']
    list_filter = ['name','status','ordering']
    search_fields=['name','title','website_link','description']

admin.site.register(Product,ProductAdmin)

class ModulesAdmin(admin.ModelAdmin):
    list_display=["product_name",'name','ordering', 'status']
    list_filter=['product_name','status','ordering']
    search_fields=['name','title','benifits_one','benifits_two','benifits_three','benifits_four','benifits_five','benifits_six','benifits_seven','benifits_eight','description_two']

admin.site.register(Modules,ModulesAdmin)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['name','description','ordering','status']
    list_filter = ['name','type','status','ordering']
    search_fields=['name','place','salary','date','type','experience','description']

admin.site.register(Vacancy,VacancyAdmin)

class Product_QAAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordering','status']
    list_filter = ['status','ordering']
    search_fields=['question','answer']

admin.site.register(Product_QA,Product_QAAdmin)

class Service_QAAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordering','status']
    list_filter = ['status','ordering']
    search_fields=['question','answer']

admin.site.register(Service_QA,Service_QAAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['module','name','phone','email','message','date']
    list_filter=['module','date']
    search_fields=['name','email','phone','message']
admin.site.register(Contact,ContactAdmin)

class Product_NameAdmin(admin.ModelAdmin):
    list_display = ['name_with_title','ordering','status']
    list_filter = ['status','ordering']
    search_fields=['name_with_title']

admin.site.register(Product_Name,Product_NameAdmin)

class ApplyJobAdmin(admin.ModelAdmin):
    list_display=["linked_jobs",'name','email','phone','resume','date']
    list_filter=['linked_jobs','date']
    search_fields=['name','email','phone','date']

admin.site.register(ApplyJob,ApplyJobAdmin)