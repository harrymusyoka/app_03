from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import secrets
from django.db.models import (Model, ForeignKey, PositiveSmallIntegerField,
        DecimalField, CharField, TextField, DateField, DateTimeField)



GENDER_TYPES = (
    ("M", "Male"),
    ("F", "Female"),
)

MARITAL_TYPES = (
    ("S", "Single"),
    ("M", "Married"),
    ("W", "Widowed"),
)


CODE_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
)

pkgdeschoice=(
  ( "SA","SNG Alone" ),
 ( "SS2","SNG Shared 2" ),
 ( "SS3","SNG Shared 3" ),
 ( "DBL","2Rms Alone" ),
 ( "DBL","2Rms Shared 2" ),
 ( "DBL","2Rms Shared 3" ),
 ( "TRA","2Rms Alone" ),
 ( "TRS2","2Rms Shared 2" ),
 ( "TRS3","2Rms Shared 3" ),
 )

rmdeschoice=(
  ( "SNG","SNG" ),
  ("1BR", "1BR"),
   ("2BR", "2BR"),
 )

stauschoice=(
  ( "cur","active" ),
  ("chkout", "chkout"),
   ("Canc", "cancelled"),
 )


rmn_CHOICES = (
    ("01", "01"),
    ("02", "02"),
    ("03", "03"),
    ("04", "04"),
    ("05", "05"),
    ("06", "06"),
    ("07", "07"),
    ("08", "08"),
    ("09", "09"),    
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
 
    
    
    
)


class CommonInfo(Model):
    created = DateTimeField("creation date", auto_now_add=True)
    modified = DateTimeField("modification date", auto_now=True)
    description = TextField()

    class Meta:
        abstract = True


class rentalunit2(models.Model):
     
     roomno = CharField(max_length=2, choices=rmn_CHOICES)                    
     roomdesc = CharField(max_length=20)
     roomtype = CharField(choices=rmdeschoice)
     rate =  models.IntegerField(default = 0)




class Client(models.Model):
    acno = models.IntegerField()
    client_name = models.CharField(max_length=40)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=40)
    email =  models.EmailField(max_length=70,blank=True,unique=True)

class Transactons(models.Model):
    acno = models.IntegerField()
    guestnumb = models.IntegerField()
    roomno= models.CharField(max_length=10)
    package =  models.CharField( max_length=12)
    amount =  DecimalField(max_digits=9, decimal_places=2, default = 0)
    date  = DateField()
    systime  = DateField()

class Receipt(models.Model):
    acno = models.IntegerField()
    guestnumb = models.IntegerField()
    roomno= models.CharField(max_length=10)
    amount =  DecimalField(max_digits=9, decimal_places=2, default = 0)
    date  = DateField()
    systime  = DateField()



class Guest(models.Model):
    Guest_name = models.CharField(max_length=50)
    IDNo = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=40)
    guestnumb = models.IntegerField()

    BirthYear = DateField()
    rate =  DecimalField(max_digits=9, decimal_places=2, default = 0)
    Gender = models.CharField( max_length=1,  choices=GENDER_TYPES,  default='X'              )
    email =   models.EmailField(max_length=70,blank=True,unique=True)
                   
    Marital = models.CharField( max_length=1, 

                    choices=MARITAL_TYPES,
                    default='X',
                   )







class accomodation_category(CommonInfo):
        code = models.CharField( max_length=1, 

                    choices=CODE_CHOICES,
                    default='0',
                   )
                  
                
        desc =models.CharField(max_length=5,
                  choices=pkgdeschoice,
                        default='SNG',
                   )
                
 
class room_category(CommonInfo):
        code = models.CharField( max_length=1, 

                    choices=CODE_CHOICES,
                    default='0',
                   )
                  
                
        desc =models.CharField(max_length=12,
                  choices=rmdeschoice,
                        default='SA',
                   )
                
 

class Checkin(models.Model):
    guestnumb = models.IntegerField()
    client_acno = models.IntegerField()
    name = models.CharField(max_length=50)
    roomno= models.CharField(max_length=10)
    package =  models.CharField( max_length=12)
    
    amount = DecimalField(max_digits=9, decimal_places=2)
    date  = DateField()
    NOPax = models.CharField( max_length=1, 

                    choices=CODE_CHOICES,
                    default='0',
                   )


class invoicedetail(models.Model):
    acno = models.IntegerField()
    guestnumb = models.IntegerField()
    name = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    roomno= models.CharField(max_length=10)
    package =  models.CharField( max_length=12)
    amount = DecimalField(max_digits=9, decimal_places=2)
    date  = DateField()



   
class rates(CommonInfo):
           Code =CharField(max_length=10)
           rate = DecimalField(max_digits=9, decimal_places=2)
           roomtype = CharField(max_length=6, default = '0')



 

class DueReceipt(CommonInfo):
    date = DateField()
    amount = DecimalField(max_digits=9, decimal_places=2,  default = 0)
    rental_unit =CharField(max_length=10, default = '0')
    guestnumb = models.IntegerField(default = 0)

class accompacks(CommonInfo):
        Code =CharField(max_length=10)
        rate  =  DecimalField(max_digits=9, decimal_places=2, default = 0)

class Receipt(CommonInfo):
    date = DateField()
    amount = DecimalField(max_digits=9, decimal_places=2,default=0)
    rental_unit =CharField(max_length=10, default = '0')
    guestnumb = models.IntegerField(default = 0)
