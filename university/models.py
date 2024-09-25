from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='kafedras', null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    bio = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    bio = models.CharField(max_length=250)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


