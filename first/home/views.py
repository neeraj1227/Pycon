from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import User,Service,Testimonial,FAQ
from django.db import connection
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
# from home.views import home



def write_sql_quries(file_path):
    with open(file_path,'w') as file:
        quries=connection.queries
        for query in quries:
            sql= query['sql']
            file.write(f"{sql}\n")
def home(request):
    #Read and fetch the data from database using Read Query
    all_records=User.objects.first()
    print(f"User:{User.location}")

    services=Service.objects.all()
    testimonial=Testimonial.objects.all()
    faqs=FAQ.objects.all()

    
    # for i in all_records:
    #     print(i.email)
   
    #create querry 
    # Student.objects.create(
    #     first_name="KApoor",
    #     email="ngtrdamg@gmai",
    #     phone=	5454451465,
    # )
    #delete Querry
    # Student.objects.get(id=15).delete()

    # file_path='sql_queries.txt'
    # write_sql_quries (file_path)
    context={
        "location":all_records.location,
        "email":all_records.email,
        "phone":all_records.phone,
        "video_url":all_records.video_url,
        "instagram_url":all_records.instagram_url,
        "facebook_url":all_records.facebook_url,
        "linkedin_url":all_records.linkedin_url,
        "github_url":all_records.github_url,

        "services":services,
        "testimonial":testimonial,
        "faqs":faqs
    }

    return render(request, 'home/home.html',context)
# User send the request to on backend
def contact_form(request):
    if request.method == 'POST':
        print("\nUser has submit a contect form\n")
        print(f"request.POST: {request.POST}")
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        print(f"name : {name}")
        print(f"email :{email}")
        print(f"subject :{subject}")
        print(f"message :{message}")

#context for email
        context={
            "name":name,
            "email":email,
            "subject":subject,
            "message":message,
        }
        html_content=render_to_string('email.html',context)
        
#sending email to reciver   
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER] ,
                fail_silently=False  #default Is True
            )
        except Exception as e:
            messages.error(request,'email is failed')
        else:
            messages.success(request,'email is successfully send')


    return redirect ('home')