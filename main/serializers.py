from rest_framework import serializers
from .models import *

class Why_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = Why_us
        fields = ('id', 'title','title_en', 'title_ru')

class Our_partnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_partners
        fields = ('id', 'image')

class Our_programsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_programs
        fields = ('id', 'title','title_en', 'title_ru','description', 'description_en', 'description_ru', 'image')

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'number', 'description', 'description_en', 'description_ru')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'title','title_en', 'title_ru','description', 'description_en', 'description_ru', 'image')

class Contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_us
        fields = ('id', 'ful_name', 'nambr', 'ischecked')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'description','description_en', 'description_ru', 'image', 'ful_name', 'title', 'title_en', 'title_ru', 'date')

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'title','title_en', 'title_ru','description', 'description_en', 'description_ru', 'title_n', 'title_n_en', 'title_n_ru', 'description_n', 'description_n_en', 'description_n_ru', 'title_a', 'title_a_en', 'title_a_ru', 'description_a', 'description_a_en', 'description_a_ru')

class For_whomSerializer(serializers.ModelSerializer):
    class Meta:
        model = For_whom
        fields = ('id', 'title','title_en', 'title_ru','description', 'description_en', 'description_ru')

class ModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modul
        fields = ('id', 'title','title_en', 'title_ru')

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id', 'lesson','lesson_en', 'lesson_ru')

class MentorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentors
        fields = ('id', 'image','title', 'title_en', 'title_ru','ful_name','description', 'description_en', 'description_ru','description_a', 'description_a_en', 'description_a_ru','description_b', 'description_b_en', 'description_b_ru','description_c', 'description_c_en', 'description_c_ru')

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('id', 'protssesor', 'protssesor_en', 'protssesor_ru','Cpu', 'Cpu_en', 'Cpu_ru', 'video_karta', 'video_karta_en', 'video_karta_ru', 'ekran', 'ekran_en', 'ekran_ru')

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('id', 'image','description', 'description_en', 'description_ru','description', 'description_en', 'description_ru','description', 'description_en', 'description_ru','description', 'description_en', 'description_ru')
class Places_of_workSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places_of_work
        fields = ('id', 'ikonka', )

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'question','question_en','question_ru', 'answer', 'answer_en', 'answer_ru')
        
