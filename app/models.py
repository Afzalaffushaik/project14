from django.db import models

# Create your models here.
class dept(models.Model):
    d_name=models.CharField(max_length=100,unique=True)
    dept_no=models.IntegerField(primary_key=True)
    dept_loc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.dept_no)

class emp(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    dept_no=models.ForeignKey(dept,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ename

class salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return str(self.grade)
