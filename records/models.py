from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class IncomingDoc(models.Model):
    book_no = models.IntegerField()
    page_no = models.IntegerField()
    year    = models.CharField(max_length=20)
    continuos_number = models.IntegerField(unique=True)
    archive_no = models.IntegerField()
    branch_no  = models.IntegerField()
    date = models.DateField(null=True, blank= True)
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    number = models.IntegerField()
    Surrender_name =models.CharField(max_length=200) 
    Surrender_date = models.DateField()
    register_number = models.IntegerField()
    remarks = models.TextField()
    image = models.ImageField(upload_to="records/images", null=True, blank=True)

    def __str__(self):
        return f"Continuous number: {self.continuos_number}"

    


