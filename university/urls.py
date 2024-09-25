from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faculties', views.faculty_list, name='faculty_list'),
    path('faculty/<int:pk>', views.faculty_detail, name='faculty_detail'),
    path('groups', views.group_list, name='group_list'),
    path('group/<int:pk>', views.group_detail, name='group_detail'),
    path('students',views.student_list,name='student_list'),
    path('student/<int:pk>',views.student_detail,name='student_detail'),
    path('kafedras',views.kafedra_list,name='kafedra_list'),
    path('kafedra/<int:pk>',views.kafedra_detail,name='kafedra_detail'),
    path('subjects', views.subject_list, name='subject_list'),
    path('subject/<int:pk>', views.subject_detail, name='subject_detail'),
    path('teachers',views.teacher_list,name='teacher_list'),
    path('teacher/<int:pk>',views.teacher_detail,name='teacher_detail'),
]
