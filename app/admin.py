from django.contrib import admin
from . models import MainCategorie,News,AboutUS,HorizontalAds,VerticalAds,SubCategorie,OurTeam,PrivacyPolicy,ContactUs




admin.site.site_header = 'Sudur News Admin Panel'        
admin.site.index_title = 'Sudur News'                
admin.site.site_title = 'Welcome to Sudur News admin panel' 


class AboutUSAdmin(admin.ModelAdmin):
    model = AboutUS
    list_display =['chairman','logo','ChiefEditor','DepartmentRegistrationNo','contactNo','email']
    
    fieldsets = (
      ('About Us', {
          'fields': ('logo','chairman','ChiefEditor','DepartmentRegistrationNo')
      }),
      ('Contact Details', {
          'fields': ('contactNo','email' )
      }),
      ('Social Media', {
          'fields': ('facebookUrl','twitterUrl','youtubeUrl' )
      })
   )
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(AboutUS,AboutUSAdmin)


class HorizontalAdsAdmin(admin.ModelAdmin):
    model = HorizontalAds
    list_display =['name','id','image','url','show','positionNumber']
    list_editable =['show','positionNumber']
admin.site.register(HorizontalAds,HorizontalAdsAdmin)

class VerticalAdsAdmin(admin.ModelAdmin):
    model = VerticalAds
    list_display =['name', 'id','image','page','show','url']
    list_editable =['show']
    list_per_page = 5
    
admin.site.register(VerticalAds,VerticalAdsAdmin)

class SubcategorieAdmin(admin.TabularInline):
    model =SubCategorie

class MainCategorieAdmin(admin.ModelAdmin):
    inlines =[SubcategorieAdmin]
    list_display = ['categorie_name','ordering']
admin.site.register(MainCategorie, MainCategorieAdmin)

# class MainCategorieAdmin(admin.ModelAdmin):
#     model = MainCategorie
#     list_display = ['categorie_name','ordering']
# admin.site.register(MainCategorie, MainCategorieAdmin)



class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display =['title','repoter','trending','feature']
    list_filter=['feature','trending']
    list_editable = ['trending','feature']
    list_per_page= 10
    
admin.site.register(News, NewsAdmin)



class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['title','contactus']
    list_editable = ['contactus']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(ContactUs, ContactUsAdmin)

class OurTeamAdmin(admin.ModelAdmin):
    model = OurTeam
    list_display = ['title','about_our_team']
    list_editable =['about_our_team']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(OurTeam,OurTeamAdmin)


class PrivacyPolicyAdmin(admin.ModelAdmin):
    model = PrivacyPolicy
    list_display =['title','privacy_policy']
    list_editable =['privacy_policy']
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    

admin.site.register(PrivacyPolicy,PrivacyPolicyAdmin)