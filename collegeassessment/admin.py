from django.contrib import admin

# from .models import Assignment,Course,Teacher,userdetail,subject
from .models import Course,Subject
# class AssignmentAdmin(admin.ModelAdmin):
#     readonly_fields=('id',)
# admin.site.register(Assignment,AssignmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Course,CourseAdmin)

# class TeacherAdmin(admin.ModelAdmin):
#     readonly_fields=('id',)

    
# admin.site.register(Teacher,TeacherAdmin)

# class UserDetailAdmin(admin.ModelAdmin):
#     readonly_fields=('id',)

    
# admin.site.register(userdetail,UserDetailAdmin)


class SubjectAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

    
admin.site.register(Subject,SubjectAdmin)
