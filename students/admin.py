from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'grade', 'created_at']
    list_filter = ['grade', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['-created_at']
