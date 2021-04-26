from django.shortcuts import render
from .models import about_model, application_model,product_model, home_model, contacts_model, contactinfo_model, newsfeed_model
from django.views.generic import ListView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_protect
def application_detail(request, id):
    
    application=application_model.objects.get(id=id)
    
    return  render(request, 'detail.html',{'application':application})

def contact(request):
    contact_info =contactinfo_model.objects.get(id=1)
    return  render(request, 'contact.html',{'contact_info':contact_info})


def about(request):
    about_top=about_model.objects.get(id=1)
    applications=application_model.objects.all()
    return  render(request, 'about.html',{'about_top':about_top, 'applications':applications})

def thanks(request):

    return  render(request, 'thanks.html',{})


def home(request):
    home_attributes=home_model.objects.all()
    newsfeed=newsfeed_model.objects.all()[:2]


    img1=None
    img2=None
    img3=None
    for home_attribute in home_attributes:
        img1=home_attribute.image1.url
        img2=home_attribute.image2.url
        img3=home_attribute.image3.url

    return  render(request, 'index.html',{'img1':img1,'img2':img2,'img3':img3,'newsfeed':newsfeed})
@csrf_protect
def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    from_email = request.POST.get('email', '')
    message= message+'\n'+'sender :{}'.format(from_email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@roza.txt'])
            contacts_model.objects.create(name=name,email=from_email,subject=subject,phone_nr=phone,message=message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/thanks')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


class ProductListView(ListView):
    model=product_model
    template_name='product.html'
    context_object_name='product'
    paginate_by=2

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        if query:
            object_list = object_list.filter(product_name__icontains=query)
            
        return object_list






