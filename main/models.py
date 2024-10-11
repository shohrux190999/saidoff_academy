from django.db import models

# Create your models here.
class Why_us(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Our_partners(models.Model):
    image = models.ImageField(upload_to='media/')

class Our_programs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title
    
class Program(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    our_partners = models.ForeignKey(Our_partners , on_delete=models.CASCADE)
    
class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    

class Contact_us(models.Model):
    ful_name = models.CharField(max_length=100)
    nambr = models.CharField(max_length=50)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    ischecked = models.BooleanField(default=False)

    
class Comment(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    ful_name = models.CharField(max_length=100)
    title = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ful_name
    
class Plan(models.Model):
    title = models.CharField(max_length=200)
    title_n = models.CharField(max_length=200)
    description_n = models.TextField()
    title_a = models.CharField(max_length=200)
    description_a = models.TextField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class For_whom(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Modul(models.Model):
    title = models.CharField(max_length=200)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
class Lessons(models.Model):
    lesson = models.CharField(max_length=200)
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE)

class Mentors(models.Model):
    image =  models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)
    ful_name = models.CharField(max_length=200)

    def __str__(self):
        return self.ful_name
    
class Computer(models.Model):
    protssesor = models.CharField(max_length=200)
    Cpu= models.CharField(max_length=200)
    video_karta = models.CharField(max_length=200)
    ekran = models.CharField(max_length=200)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.protssesor

class Mentor(models.Model):
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    description = models.TextField()
    description = models.TextField()
    description = models.TextField()
    mentors = models.ForeignKey(Mentors, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Places_of_work(models.Model):
    ikonka = models.ImageField(upload_to='media/')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
