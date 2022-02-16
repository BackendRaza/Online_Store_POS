from django.db import models

class Person(models.Model):
    pname = models.CharField(max_length = 50)
    plocation = models.CharField(max_length = 50)

    class Meta:
        db_table = "Person"

'''class userLogin(models.Model):
    uname =  models.CharField(max_length = 50)
    upass =  models.CharField(max_length = 50)'''

class custinfo(models.Model):
    cfname = models.CharField(max_length = 50)
    cmail = models.CharField(max_length = 50)
    cpass = models.CharField(max_length = 50)
    ccontact = models.CharField(max_length = 50)

    class Meta:
        db_table = "custinfo"

###################################PRODUCTS#######################################

class Catagory(models.Model):
    catname =  models.CharField(max_length = 50)
    def __str__(self):
        return self.catname

    class Meta:
        db_table = "Catagory"

class subCatagory(models.Model):
    subcatname = models.CharField(max_length = 50)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    def __str__(self):
        return self.subcatname

    class Meta:
        db_table = "subCatagory"

class products(models.Model):
    pname = models.CharField(max_length = 50)
    pdesc = models.CharField(max_length = 50)
    prate = models.FloatField(default= 0)
    pimage = models.ImageField(upload_to = 'Images', default = 'Select Pic')
    subcat = models.ForeignKey(subCatagory, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

#####################Cart################################
class CartDetails(models.Model):
    user = models.ForeignKey(custinfo, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)