from django.contrib import admin
from .models import *


# Register your models here.
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = '__all__'


class UserAdmin(admin.ModelAdmin):
    list_display = '__all__'


class PolicyAdmin(admin.ModelAdmin):
    list_display = '__all__'


class ClaimAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(RegisterUser)
admin.site.register(User)
admin.site.register(Policy)
admin.site.register(Claim)
