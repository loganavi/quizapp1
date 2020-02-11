from django.contrib import admin
from QuizApp.models import contact_form
# Register your models here.

class contact_form_Admin(admin.ModelAdmin):
	list_display=['Name','Email','Subject','Message']
admin.site.register(contact_form,contact_form_Admin)