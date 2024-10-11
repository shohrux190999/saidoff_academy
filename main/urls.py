from django.urls import path
from .views import *


urlpatterns = [
    path('why_us/', Why_usList.as_view(), name='why_us_list'),
    path('our_partners/', Our_partnersList.as_view(), name='our_partners_list'),
    path('our_programs/', Our_programsList.as_view(), name='our_programs_list'),
    path('courses/', CoursesList.as_view(), name='courses_list'),
    path('contact_us/', Contact_usCreate.as_view(), name='contact_us_create'),
    path('comment/', CommentList.as_view(), name='comment_list'),
    path('faq/', FaqList.as_view(), name='faq_list'),
    path('mentors/', MentorsList.as_view(), name='mentors_list'),
    path('plan/<int:pk>/', PlanRetrieve.as_view(), name='plan_retrieve'),
    path('modul/<int:pk>/', ModulList.as_view(), name='modul_retrieve'),
    path('lessons/', LessonsList.as_view(), name='lessons_list'),
    path('mentor/<int:pk>/', MentorRetrive.as_view(), name='mentor_retrieve'),
    path('computer/<int:pk>/', MentorRetrive.as_view(), name='computer_retrieve'),
    path('for_whom/', For_whom_list.as_view(), name='for_whom_list'),
    path('Program/', ProgramList.as_view(), name='program'),
]