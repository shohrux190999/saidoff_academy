from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Why_us)
class Why_usTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Our_programs)
class Our_programsTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('description', 'title')

@register(For_whom)
class For_whomTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Plan)
class PlanTranslationOptions(TranslationOptions):
    fields = ('title','title_n', 'description_n', 'title_a', 'description_a')


@register(Modul)
class ModulTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Lessons)
class LessonsTranslationOptions(TranslationOptions):
    fields = ('lesson',)

@register(Mentors)
class MentorsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Computer)
class ComputerTranslationOptions(TranslationOptions):
    fields = ('protssesor','Cpu', 'video_karta', 'ekran',)


@register(Mentor)
class MentorTranslationOptions(TranslationOptions):
    fields = ('description','description','description','description')

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')



