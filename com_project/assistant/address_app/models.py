from django.db import models


# Create your models here.
class Contact(models.Model):
    nickname = models.CharField(max_length=50, null=False)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname


class Info(models.Model):
    nickname = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    birthday = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=False)

    contacts = models.ManyToManyField(Contact, through='ContactToInfo')

    def __str_(self):
        return f'{self.nickname} - {self.name} {self.surname}'


class ContactToInfo(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
