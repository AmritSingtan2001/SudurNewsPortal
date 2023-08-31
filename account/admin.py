from django.contrib import admin
from account.models import User
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

    
class UserModelAdmin(BaseUserAdmin):
  list_display = ('id', 'email', 'fullname','image' ,'phone_No','is_editor','is_staff','is_superuser')
  list_filter = ('is_editor',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('fullname', 'phone_No','image')}),
      ('Permissions', {'fields': ( 'groups', 'user_permissions','is_editor')}),
  )
  
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'fullname','image', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')


admin.site.register(User, UserModelAdmin)