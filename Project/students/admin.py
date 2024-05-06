from django.contrib import admin
from .models import Student, Question

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("studentID", "lastname", "firstname", "phone", "birthday")
admin.site.register(Student, StudentAdmin)
admin.site.register(Question)
