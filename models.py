from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True)
    utype = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)

class Branch(models.Model):
    branchname = models.CharField(max_length=100)
    village = models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Emp(models.Model):
    employee_id=models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    employee_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    parent_mobile = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    previous_company = models.CharField(max_length=200, blank=True, null=True)
    work_start_date = models.DateField(blank=True, null=True)
    work_end_date = models.DateField(blank=True, null=True)
    reason_leaving = models.TextField(blank=True, null=True)
    aadhaar_document = models.FileField(upload_to='documents/', blank=True, null=True)
    pancard = models.FileField(upload_to='documents/', blank=True, null=True)
    bank_document = models.FileField(upload_to='documents/', blank=True, null=True)
    passport_size_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    pincode = models.CharField(max_length=100)
    branchname = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name


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
    customer_id = models.CharField(max_length=50)
    product = models.CharField(max_length=50)


class Dealer(models.Model):
    dealer_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)  # Adjust max_length as needed
    email = models.EmailField(max_length=50)
    document = models.CharField(max_length=50)
    village=models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    gst = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    Itemname = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    part_no = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    dispatch = models.CharField(max_length=100)

    branchname=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Stock(models.Model):
    Itemname = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    part_no = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    dispatch = models.CharField(max_length=100)
    branchname=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookingItem(models.Model):
    customername = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    branchname = models.CharField(max_length=100)
    itemname =models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    totalAmount = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)
    totalamount = models.CharField(max_length=100)
    village = models.CharField(max_length=50)
    Taluk = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)


class Stock(models.Model):
    Itemname = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    part_no = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    dispatch = models.CharField(max_length=100)
    branchname=models.CharField(max_length=100)

class CustomerBalance(models.Model):
    customername = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branchname = models.CharField(max_length=100)
    itemname =models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    totalAmount = models.CharField(max_length=100)
    booking_date = models.CharField(max_length=100)
    accountholder = models.CharField(max_length=100)
    accountnumber = models.CharField(max_length=100)
    upiId = models.CharField(max_length=100)
    transactionId = models.CharField(max_length=100)
    pay_status = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)
    entry_amount=models.CharField(max_length=100)
    paymentMode = models.CharField(max_length=100)



class Transfer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField()
    branch_from = models.CharField(max_length=100)  # From Branch
    branch_to = models.CharField(max_length=100)  # To Branch
    # Other fields...

    def __str__(self):
        return f"{self.qty} of {self.item.Itemname} transferred to {self.branch}"

class BranchItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    qty = models.IntegerField()


class Subsidy(models.Model):
    customer_name = models.CharField(max_length=255)
    rtsg_amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_date = models.DateField()
    bill_a = models.CharField(max_length=255)
    bill_b = models.CharField(max_length=255)
    utr_number = models.CharField(max_length=255)

    def __str__(self):
        return f"Subsidy for {self.customer.name} on {self.entry_date}"

class Employee_register(models.Model):
    employee_id=models.CharField(max_length=200)
    employee_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    parent_mobile = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    previous_company = models.CharField(max_length=200, blank=True, null=True)
    work_start_date = models.DateField(blank=True, null=True)
    work_end_date = models.DateField(blank=True, null=True)
    reason_leaving = models.TextField(blank=True, null=True)
    aadhaar_document = models.FileField(upload_to='documents/', blank=True, null=True)
    pancard = models.FileField(upload_to='documents/', blank=True, null=True)
    bank_document = models.FileField(upload_to='documents/', blank=True, null=True)
    passport_size_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    pincode = models.CharField(max_length=100)
    branchname = models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    dob = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    doj = models.CharField(max_length=200)
    tenth_qualification = models.CharField(max_length=200)
    tenth_passout_year = models.CharField(max_length=200)
    tenth_percentage = models.CharField(max_length=200)
    twelfth_qualification = models.CharField(max_length=200)
    twelfth_passout_year = models.CharField(max_length=200)
    twelfth_percentage = models.CharField(max_length=200)
    degree_qualification = models.CharField(max_length=200)
    degree_passout_year = models.CharField(max_length=200)
    degree_percentage = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    jobrole = models.CharField(max_length=200)
    pf = models.CharField(max_length=200)
    esic = models.CharField(max_length=200)
    sallery=models.CharField(max_length=200)
    adhar=models.CharField(max_length=200)
    pan = models.CharField(max_length=200)
    experienceletter= models.CharField(max_length=200)
