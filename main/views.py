from django.shortcuts import render
from django.shortcuts import render
from.models import *
from .serializers import *
from rest_framework import generics


# Create your views here.


class Why_usList(generics.ListAPIView):
    queryset = Why_us.objects.all()
    serializer_class = Why_usSerializer


class Our_partnersList(generics.ListAPIView):
    queryset = Our_partners.objects.all()
    serializer_class = Our_partnersSerializer


class Our_programsList(generics.ListAPIView):
    queryset = Our_programs.objects.all()
    serializer_class = Our_programsSerializer


class CoursesList(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class Contact_usCreate(generics.CreateAPIView):
    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FaqList(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class MentorsList(generics.ListAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorsSerializer

class PlanRetrieve(generics.RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class ModulList(generics.ListAPIView):
    queryset = Modul.objects.all()
    serializer_class = ModulSerializer

class LessonsList(generics.ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer

class MentorRetrive(generics.RetrieveAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorsSerializer

class ComputerRetrive(generics.RetrieveAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class ProgramList(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class For_whom_list(generics.ListAPIView):
    queryset = For_whom.objects.all()
    serializer_class = For_whomSerializer



