from django.db import models

# Create your models here.


class Branch(models.Model):
    branchname = models.CharField(max_length=100)
    village = models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype=models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    branchname = models.CharField(max_length=50)




class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adhar = models.CharField(max_length=50)
    pancard = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    previoucompany = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    sallery = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    jrole = models.CharField(max_length=50)
    doj = models.CharField(max_length=50)
    pf = models.CharField(max_length=50)
    esic = models.CharField(max_length=50)
    adhar_doc = models.FileField(upload_to='pdfs/')
    pan_doc = models.FileField(upload_to='pdfs/')
    bank_doc = models.FileField(upload_to='pdfs/')
    exp_doc = models.FileField(upload_to='pdfs/')
    tenthpass = models.CharField(max_length=50)
    tenth_percentage = models.CharField(max_length=50)
    twelfth_pass = models.CharField(max_length=50)
    twelfth_percentage = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    degreepass = models.CharField(max_length=50)
    degree_percentage = models.CharField(max_length=50)
    pf = models.CharField(max_length=50)
    esic = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    account_holder_name = models.CharField(max_length=100, blank=True, null=True)
    emp_id = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    branchname = models.CharField(max_length=100)


class Item(models.Model):
    Itemname = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.CharField(max_length=100)
    part_no = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    godown = models.CharField(max_length=100)
    branchname=models.CharField(max_length=100)

class TransferredItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='transfers')  # Link to the Item model
    quantity = models.IntegerField()
    source_branch = models.CharField(max_length=255)
    destination_branch = models.CharField(max_length=255)
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.itemname} transferred from {self.source_branch} to {self.destination_branch}'


class Stock(models.Model):
    Itemname = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.CharField(max_length=100)
    part_no = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    branchname=models.CharField(max_length=100)


class Transfer(models.Model):
    item = models.ForeignKey('Stock', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    source_branch = models.CharField(max_length=255)
    destination_branch = models.CharField(max_length=255)
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.Itemname} from {self.source_branch} to {self.destination_branch}"




class Customer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    branchname = models.CharField(max_length=50)
    employeename = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    customer_id = models.IntegerField()
    product = models.CharField(max_length=50)
    state = models.CharField(max_length=50)



class Dealer(models.Model):
    Firm_name = models.CharField(max_length=50)
    Owner_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    gst = models.CharField(max_length=50)
    adhar = models.IntegerField()
    pan = models.CharField(max_length=50)
    adhar_document = models.FileField(upload_to='pdfs/')
    pan_document = models.FileField(upload_to='pdfs/')
    bank_document = models.FileField(upload_to='pdfs/')
    gst_doc = models.FileField(upload_to='pdfs/')
    contact = models.CharField(max_length=50)