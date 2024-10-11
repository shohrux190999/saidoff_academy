from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class Why_usAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'image')
admin.site.register(Why_us,Why_usAdmin)

class Our_partnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
admin.site.register(Our_partners, Our_partnersAdmin)

class Our_programsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'image')
admin.site.register(Our_programs, Our_programsAdmin)

class ProgramAdmin(TranslationAdmin):
    list_display = ('id', 'number', 'description', )
admin.site.register(Program, ProgramAdmin)

class CoursesAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'image')
admin.site.register(Courses, CoursesAdmin)

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'ful_name', 'nambr','ischecked', )
admin.site.register(Contact_us, Contact_usAdmin)

class CommentAdmin(TranslationAdmin):
    list_display = ('id', 'description', 'image', 'ful_name', 'title', 'date')
admin.site.register(Comment, CommentAdmin)

class PlanAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'title_n', 'description_n', 'title_a', 'description_a')
admin.site.register(Plan, PlanAdmin)

class For_whomAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
admin.site.register(For_whom, For_whomAdmin)

class ModulAdmin(TranslationAdmin):
    list_display = ('id', 'title',)
admin.site.register(Modul, ModulAdmin)

class LessonsAdmin(TranslationAdmin):
    list_display = ('id', 'lesson')
admin.site.register(Lessons, LessonsAdmin)

class MentorsAdmin(TranslationAdmin):
    list_display = ('id', 'image', 'title', 'ful_name')
admin.site.register(Mentors, MentorsAdmin)

class ComputerAdmin(TranslationAdmin):
    list_display = ('id', 'protssesor','Cpu', 'video_karta', 'ekran', )
admin.site.register(Computer, ComputerAdmin)

class MentorAdmin(TranslationAdmin):
    list_display = ('id', 'image', 'description', 'description', 'description', 'description',)
admin.site.register(Mentor, MentorAdmin)

class Places_of_workAdmin(admin.ModelAdmin):
    list_display = ('id', 'ikonka',)
admin.site.register(Places_of_work, Places_of_workAdmin)

class FaqAdmin(TranslationAdmin):
    list_display = ('id', 'question', 'answer')
admin.site.register(Faq, FaqAdmin)




