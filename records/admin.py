from django.contrib import admin
from .models import IncomingDoc, OutgoingDoc
# Register your models here.

admin.site.register(IncomingDoc)
admin.site.register(OutgoingDoc)
