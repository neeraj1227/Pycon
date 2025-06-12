from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .models import User,Service,Testimonial
from django.db import connection
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

        "Service":Service,
        "Testimonial":Testimonial
    }
    print(f"context :{context}")


    return render(request, 'home/home.html',context)

# def contact(request):
    
#     return render(request,'home/contact.html',context ={'page':"contact"})

# def about(request):
#     return render(request,"home/about.html",context ={'page':"about"}) 