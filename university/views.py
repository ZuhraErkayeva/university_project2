from django.shortcuts import render, get_object_or_404
from .models import Faculty, Group, Student, Subject, Teacher, Kafedra


def faculty_list(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}
    return render(request, 'faculty-list.html', ctx)


def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    ctx = {'faculty': faculty}
    return render(request, 'faculty-detail.html', ctx)


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'group-list.html', ctx)
def group_detail(request,pk):
    group = get_object_or_404(Group,pk=pk)
    ctx = {'group': group}
    return render(request,'group-detail.html',ctx)


def home(request):
    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'student-list.html', ctx)

def student_detail(request,pk):
    student = get_object_or_404(Student,pk=pk)
    ctx = {'student': student}
    return render(request,'student-detail.html',ctx)
def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subject-list.html', ctx)
def subject_detail(request,pk):
    subject = get_object_or_404(Subject,pk=pk)
    ctx = {'subject': subject}
    return render(request,'subject-detail.html',ctx)


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teacher-list.html', ctx)

def teacher_detail(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    ctx = {'teacher': teacher}
    return render(request,'teacher-detail.html',ctx)
def kafedra_list(request):
    kafedras = Kafedra.objects.all()
    ctx = {'kafedras': kafedras}
    return render(request, 'teacher-list.html', ctx)
def kafedra_detail(request,pk):
    kafedra = get_object_or_404(Kafedra,pk=pk)
    ctx = {'kafedra': kafedra}
    return render(request,'kafedra-detail.html',ctx)
