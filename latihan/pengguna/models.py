from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telpon = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='pengguna', blank=True, null=True)

    def _str_(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "1. Biodata"
    
#one to one
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    # Other fields

class Passport(models.Model):
    passport_number = models.CharField(max_length=20)
    expiration_date = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_number

# Penjelasan Relasi One To One : 
# Di sini, kita memiliki dua model: Person dan Passport. Hubungan satu ke satu 
# didefinisikan oleh bidirectional one to one relationship antara Person dan Passport. 
# Setiap orang memiliki satu paspor, dan setiap paspor terkait dengan satu orang. 


#one to many
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    # Other fields

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Other fields

    def __str__(self):
        return self.name

# Penjelasan Relasi One To Many :
# Di sini, kita memiliki dua model: Department dan Employee. Hubungan satu ke banyak 
# didefinisikan oleh field ForeignKey pada model Employee, yang menunjuk ke model Department. 
# Setiap departemen dapat memiliki banyak karyawan, tetapi setiap karyawan hanya terdaftar di satu departemen.


#many to many
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Other fields

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    # Other fields

    def __str__(self):
        return self.name
        
# Penjelasan Relasi Many To Many :
# Di sini, kita memiliki dua model: Student dan Course. Hubungan banyak ke banyak 
# didefinisikan oleh field ManyToManyField pada model Course, yang menunjuk ke model Student. 
# Seorang mahasiswa dapat mendaftar dalam banyak kursus, dan satu kursus dapat memiliki banyak mahasiswa.
