"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import home,contact_form
# from django.http import HttpResponseRedirect
# def go_to_github(request):
#     return HttpResponseRedirect('https://github.com/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('',include('home.urls')),
    path('contact/', contact_form,name="contact_form")
    # path('github/', go_to_github, name='github_redirect'),
    # path('about/',)
    # path("__reload__/", include("django_browser_reload.urls"))
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


