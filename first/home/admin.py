from django.contrib import admin
from home.models import User,Service,Testimonial,FAQ

# admin.site.register(Student)
# admin.site.register(Musician)
# admin.site.register(Album)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =[
        'first_name',
        'location',
        'email',
        'phone',
        'video_url',
        'facebook_url',
        'instagram_url',
        
    ]
    search_fields=[
        'first_name'
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=[
        'icon',
        'title',
        'description',
    ]
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=[
        
        'name',
        'profession',
        'display_rating',
       
    ]

    def display_rating(self,obj):
        return '*'* obj.rate
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=[
        'question'
    ]
    
    #show  to disable and permission
    # def has_add_permission(self, request, obj=None):
    #     return False
    #show to disable update permission
    # def has_change_permission(self, request, obj =None):
    #     return False
    #show to disable delete permission
    # def has_delete_permission(self, request, obj =None):
    #     return False
    # readonly_fields=[
    #         'email'
    #     ]
