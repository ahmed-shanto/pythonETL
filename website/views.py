from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    company_details=Company_Details.objects.all()
    static_files=Static_Files.objects.all()
    exclusive_features=Exclusive_Features.objects.filter(status = True).order_by("ordering")
    home_products=Home_Products.objects.filter(status = True).order_by("ordering")
    home_features=Home_Features.objects.filter(status = True).order_by("ordering")
    clients=Clients.objects.filter(status = True).order_by("ordering")
    events=Events.objects.filter(status=True).order_by("ordering")
    
    context = {
    'company_details':company_details,
    'static_files':static_files,
    'exclusive_features':exclusive_features,
    'home_products':home_products,
    'clients':clients,
    'events':events,
    'home_features':home_features

    }
    return render(request, 'website/index.html',context)

def about_us(request):
    company_details=Company_Details.objects.all()
    about_count=About_Count.objects.filter(status=True).order_by("ordering")
           
    context = {
        'company_details':company_details,
        'about_count':about_count,

    }
    return render(request, 'website/about.html',context)

def contact(request):
    company_details=Company_Details.objects.all()
           
    context = {
    'company_details':company_details
    }

    if request.method == 'POST' :
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact.objects.create(name=name,phone=phone,email=email,message=message)
       

    return render(request, 'website/contact.html',context)

def services(request):
    company_details=Company_Details.objects.all()
    services=Services.objects.filter(status=True).order_by("ordering")
    static_files=Static_Files.objects.all()
    service_qa=Service_QA.objects.filter(status=True).order_by("ordering")   
    context = {
        'services':services,
        'static_files':static_files,
        'service_qa':service_qa,
        'company_details':company_details

    }
    return render(request, 'website/services.html',context)

def products(request):
    company_details=Company_Details.objects.all()
    product=Product.objects.filter(status=True).order_by("ordering")
    product_name=Product_Name.objects.filter(status=True).order_by("ordering")
    modules=Modules.objects.filter(status=True).order_by("ordering")
    static_files=Static_Files.objects.all()
    product_qa=Product_QA.objects.filter(status=True).order_by("ordering")
           
    context = {
        'company_details':company_details,
        'product':product,
        'product_name':product_name,
        'modules':modules,
        'static_files':static_files,
        'product_qa':product_qa,
    }
    return render(request, 'website/products.html',context)


@ csrf_exempt
def career(request):
    company_details=Company_Details.objects.all()
    vacancy=Vacancy.objects.filter(status=True).order_by("ordering") 
    applyjob=ApplyJob.objects.all()

           
    context = {
        'vacancy':vacancy,
        'company_details':company_details,
        'applyjob':applyjob,

    }

    if request.method == 'POST':
        job_id=request.POST.get('job_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES.get('resume')
        print("job_id", job_id)
        ApplyJob.objects.create(linked_jobs_id=job_id,name = name, email=email,phone=phone,resume=resume)
        

    return render(request, 'website/career.html',context)
def module(request,name):
    product=Product.objects.filter(status=True).order_by("ordering")
    product_name=Product_Name.objects.filter(status=True).order_by("ordering")
    modules=Modules.objects.filter(status=True).order_by("ordering")
    
   
    module= name.replace('-', ' ')
    filter_data = Modules.objects.filter(name__icontains=module)


    context = {
        'product':product,
        'product_name':product_name,
        'modules':modules,
        'name':name,
        'filter_data':filter_data,
        "name":module,
    }
    if request.method == 'POST' :
        name=request.POST.get('name')
        module_id=request.POST.get('module_id')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        # print("f", request.POST.get('module_id'))
        Contact.objects.create(module_id = module_id ,name=name,phone=phone,email=email,message=message)

    return render(request, 'website/module.html',context)

