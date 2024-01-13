from django.db import models

# Create your models here.


class IncomingDoc(models.Model):
    continuos_number = models.IntegerField(unique=True)
    book_no = models.IntegerField()
    page_no = models.IntegerField()
    year    = models.CharField(max_length=20, null=True, blank=True)
    archive = models.CharField(max_length=200, null=True, blank=True)
    branch  = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank= True)
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    number = models.IntegerField()
    Surrender_name =models.CharField(max_length=200) 
    Surrender_date = models.DateField()
    register_number = models.IntegerField()
    remarks = models.TextField()
    image = models.ImageField(upload_to="records/incomingdocs/images", null=True, blank=True)

    def __str__(self):
        return f"Continuous number: {self.continuos_number}"

    

class OutgoingDoc(models.Model):
    continuos_number = models.IntegerField(unique=True)
    date = models.DateField(null=True, blank=True)
    book_no = models.IntegerField()
    page_no = models.IntegerField()
    year    = models.CharField(max_length=20, null=True, blank=True)
    archive = models.CharField(max_length=200, null=True, blank=True)
    branch  = models.CharField(max_length=200, null=True, blank=True)
    short_explain = models.TextField()
    dossier_no = models.IntegerField()
    image = models.ImageField(upload_to="records/outgoingdocs/images", null=True, blank=True)

    def __str__(self):
        return f"Continuous number: {self.continuos_number}"


    

