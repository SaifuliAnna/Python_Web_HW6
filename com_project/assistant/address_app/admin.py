from django.contrib import admin
from .models import Contact, Info, ContactToInfo


# Register your models here.
admin.site.register(Contact)
admin.site.register(Info)
admin.site.register(ContactToInfo)
