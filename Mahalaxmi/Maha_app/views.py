import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Maha_app.models import Branch,Login,Employee,Item,Stock,Transfer,Customer,Dealer
from pyexpat.errors import messages

from django.db.models import Max
from setuptools import logging
from setuptools.config._validate_pyproject import ValidationError


# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            udata = Login.objects.get(username=username)
            if password == udata.password:  # Use hashed password checks in production
                request.session['username'] = username
                request.session['utype'] = udata.utype

                if udata.utype == 'user':
                    return redirect('index')  # Redirect to a user-specific page
                if udata.utype == 'admin':
                    return redirect('admin_dashboard')  # Adjust as necessary
                if udata.utype == 'employee':
                    return redirect('emp_dashboard')  # Adjust as necessary
            else:
                messages.error(request, 'Invalid password')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid Username')

    return render(request, 'index.html')



def emp_dashboard(request):
    return render(request,'emp_dashboard.html')


def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def admin_nav(request):
    return render(request,'admin_nav.html')


def branch(request):
    if request.method == 'POST':
        branchname = request.POST.get('branchname')
        village = request.POST.get('village')
        Taluk = request.POST.get('Taluk')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        # Save branch to the database
        Branch.objects.create(branchname=branchname, village=village, Taluk=Taluk, district=district, state=state, pincode=pincode)

        return redirect('branch')  # Adjust this redirect as needed

    return render(request, 'branch.html')


def branch_list(request):
    branches = Branch.objects.all()  # Fetch all branch records from the database
    return render(request, 'branch_list.html', {'branches': branches})




def edit_branch(request, branch_id):
    # Get the branch object to edit
    branch = get_object_or_404(Branch, id=branch_id)

    # Handle form submission
    if request.method == 'POST':
        # Manually retrieve and update the branch fields
        branch.branchname = request.POST.get('branchname')
        branch.village = request.POST.get('village')
        branch.Taluk = request.POST.get('Taluk')
        branch.district = request.POST.get('district')
        branch.pincode = request.POST.get('pincode')
        branch.state = request.POST.get('state')
        branch.save()
        return redirect('branch_list')  # Redirect to the branch list after saving

    # Prepopulate form fields for the GET request
    return render(request, 'edit_branch.html', {'branch': branch})


def employee(request):
    if request.method == 'POST':
        # Get employee details from the form
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')
        nationality = request.POST.get('nationality')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        district = request.POST.get('district')
        Taluk = request.POST.get('Taluk')
        email = request.POST.get('email')
        adhar = request.POST.get('adhar')
        pancard = request.POST.get('pancard')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        occupation = request.POST.get('occupation')
        previoucompany = request.POST.get('previoucompany')
        role = request.POST.get('role')
        sallery = request.POST.get('sallery')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        jrole = request.POST.get('jrole')
        doj = request.POST.get('doj')
        pf = request.POST.get('pf')
        esic = request.POST.get('esic')
        tenthpass = request.POST.get('tenthpass')
        tenth_percentage = request.POST.get('tenth_percentage')
        twelfth_pass = request.POST.get('twelfth_pass')
        twelfth_percentage = request.POST.get('twelfth_percentage')
        degree = request.POST.get('degree')
        degreepass = request.POST.get('degreepass')
        degree_percentage = request.POST.get('degree_percentage')
        bank_name = request.POST.get('bank_name')
        bank_account_number = request.POST.get('bank_account_number')
        ifsc_code = request.POST.get('ifsc_code')
        account_holder_name = request.POST.get('account_holder_name')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        emp_id = generate_employee_id()  # You need to implement this function

        # Get the branch selected by the user
        branch_id = request.POST.get('branchname')

        # File uploads
        adhar_doc = request.FILES.get('adhar_doc')
        pan_doc = request.FILES.get('pan_doc')
        bank_doc = request.FILES.get('bank_doc')
        exp_doc = request.FILES.get('exp_doc')
        photo = request.FILES.get('photo')

        # Save Employee object
        employee = Employee.objects.create(
            fullname=fullname,
            gender=gender,
            dob=dob,
            contact=contact,
            nationality=nationality,
            city=city,
            state=state,
            pincode=pincode,
            district=district,
            Taluk=Taluk,
            email=email,
            adhar=adhar,
            pancard=pancard,
            fathername=fathername,
            mothername=mothername,
            occupation=occupation,
            previoucompany=previoucompany,
            role=role,
            sallery=sallery,
            start_date=start_date,
            end_date=end_date,
            jrole=jrole,
            doj=doj,
            pf=pf,
            esic=esic,
            adhar_doc=adhar_doc,
            pan_doc=pan_doc,
            bank_doc=bank_doc,
            exp_doc=exp_doc,
            tenthpass=tenthpass,
            tenth_percentage=tenth_percentage,
            twelfth_pass=twelfth_pass,
            twelfth_percentage=twelfth_percentage,
            degree=degree,
            degreepass=degreepass,
            degree_percentage=degree_percentage,
            photo=photo,
            bank_name=bank_name,
            bank_account_number=bank_account_number,
            ifsc_code=ifsc_code,
            account_holder_name=account_holder_name,
            password=password,
            emp_id=emp_id,
            branchname=branch_id,
            mobile=mobile# Save the selected branch
        )

        # Save Login details
        Login.objects.create(
            username=emp_id,
            password=password,
            utype='employee',
            employee_name=fullname
        )

        return redirect('employee')  # Redirect after saving, adjust URL as needed

    # Get all branches from the database to display in the form
    branches = Branch.objects.all()

    return render(request, 'employee.html', {'branches': branches})


def check_contact(request):
    contact = request.GET.get('contact')  # Retrieve the contact number from the GET request
    if Employee.objects.filter(contact=contact).exists():
        return JsonResponse({'exists': True})
    else:
        return JsonResponse({'exists': False})
def generate_employee_id():
    # Fetch the last employee_id (max value) from the Employee model
    last_employee = Employee.objects.aggregate(max_id=Max('emp_id'))
    last_id = last_employee['max_id']

    # Check if we have any employees
    if last_id and last_id.startswith('M'):
        # Extract the numeric part from the last employee ID, e.g., M01 -> 1
        numeric_part = int(last_id[1:])  # Strip the 'M' and convert to int
        new_numeric_part = numeric_part + 1
    else:
        new_numeric_part = 1  # Start from M01 if no employee exists

    # Generate the new employee ID with the 'M' prefix and leading zero padding
    new_employee_id = f'M{new_numeric_part:02d}'  # E.g., M01, M02, etc.
    return new_employee_id
 # Ensure you have this utility


def emp_list(request):
    # Fetch all employees
    employees = Employee.objects.all()

    # Pass the employees list to the template
    return render(request, 'emp_list.html', {'employees': employees})


def edit_employee(request, id):
    # Retrieve the employee object based on the provided ID
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        # Update employee fields directly from the POST data
        employee.fullname = request.POST.get('fullname')
        employee.gender = request.POST.get('gender')
        employee.email = request.POST.get('email')
        employee.city = request.POST.get('city')
        employee.state = request.POST.get('state')
        employee.taluk = request.POST.get('taluk')
        employee.district = request.POST.get('district')
        employee.pincode = request.POST.get('pincode')
        employee.contact = request.POST.get('contact')
        employee.role = request.POST.get('role')

        # Save the updated employee object
        employee.save()
        return redirect('employee_list')  # Redirect to the employee list page

    # Render the edit employee form template with the current employee data
    return render(request, 'edit_employee.html', {'employee': employee})

def view_certificate(request, id):
    employee = get_object_or_404(Employee, pk=id)
    return render(request, 'view_certificate.html', {'employee': employee})

    # Render the template with the employee data
    return render(request, 'employee_view.html', {'employee': employee})



def add_item(request):
    if request.method == 'POST':
        Itemname = request.POST.get('Itemname')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        part_no = request.POST.get('part_no')
        description = request.POST.get('description')
        godown = request.POST.get('godown')
        branch_id = request.POST.get('branchname')

        # Create a new item in the Item model
        item = Item.objects.create(
            Itemname=Itemname,
            qty=qty,
            price=price,
            part_no=part_no,
            description=description,
            godown=godown,
            branchname=branch_id
        )

        # Create a new entry in the Stock model
        stock = Stock.objects.create(
            Itemname=Itemname,
            qty=qty,
            price=price,
            part_no=part_no,
            description=description,
            branchname=branch_id
        )

        return redirect('add_item')  # Redirect to item list page

    # Fetching all branches to display in the dropdown
    branches = Branch.objects.all()

    # For an existing item, you will need to prepopulate the fields
    item = Item()  # Set to a new instance initially, or populate based on `id` if editing

    return render(request, 'add_item.html', {'branches': branches, 'item': item})





def item_list(request):
    # Fetch all items from the database
    items = Item.objects.all()

    # Pass items to the template
    return render(request, 'item_list.html', {'items': items})


def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_list.html', {'stocks': stocks})

def item_view(request):
    if request.method == 'POST':
        # Receive the AJAX data
        data = json.loads(request.body)
        item_id = data.get('item_id')
        transfer_qty = int(data.get('transfer_qty'))
        destination_branch = data.get('destination_branch')

        try:
            # Fetch the stock item for the source branch
            source_stock = Stock.objects.get(id=item_id)

            # Check if sufficient quantity is available
            if source_stock.qty >= transfer_qty:
                # Reduce stock from source branch
                source_stock.qty -= transfer_qty
                source_stock.save()

                # Check if the destination branch already has the item
                destination_stock, created = Stock.objects.get_or_create(Itemname=source_stock.Itemname, branchname=destination_branch)

                # Increase stock in destination branch
                destination_stock.qty += transfer_qty
                destination_stock.save()

                # Save the transfer record
                transfer = Transfer.objects.create(
                    item=source_stock,
                    quantity=transfer_qty,
                    source_branch=source_stock.branchname,
                    destination_branch=destination_branch
                )

                # Fetch the updated list of items
                updated_items = Stock.objects.all().values('id', 'Itemname', 'qty', 'price', 'part_no', 'description', 'branchname')

                return JsonResponse({
                    'status': 'success',
                    'message': f"Successfully transferred {transfer_qty} of {source_stock.Itemname} from {source_stock.branchname} to {destination_branch}.",
                    'updated_items': list(updated_items),
                    'transfer': {
                        'item': source_stock.Itemname,
                        'quantity': transfer_qty,
                        'source_branch': source_stock.branchname,
                        'destination_branch': destination_branch,
                        'transfer_date': transfer.transfer_date.strftime('%Y-%m-%d %H:%M:%S')
                    }
                })

            else:
                return JsonResponse({'status': 'error', 'message': 'Insufficient stock in the source branch.'})

        except Stock.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Source stock not found.'})

    # If not POST, render the page with all items
    items = Stock.objects.all()
    branches = Branch.objects.all()  # Fetching branches to show in the dropdown
    return render(request, 'item_view.html', {'items': items, 'branches': branches})


def transfer_item_list(request):
    # Get all transfer records from the database
    transfers = Transfer.objects.all()

    # Prepare the context to pass to the template
    context = {
        'transfers': transfers
    }

    return render(request, 'transfer_item_list.html', context)


def customer(request):
    if request.method == 'POST':
        # Fetch the last customer
        last_customer = Customer.objects.last()  # Assuming you're using a model called `Customer`

        if last_customer and last_customer.customer_id:
            # If there is a last customer and the customer_id is not empty, increment it
            new_id = int(last_customer.customer_id) + 1
        else:
            # If no last customer or customer_id is empty, start with 1
            new_id = 1

        # Now you can use new_id safely
        # Proceed with creating a new customer or handling the request further
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        village = request.POST.get('village')
        Taluk = request.POST.get('Taluk')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        product = request.POST.get('product')
        branchname = request.POST.get('branchname')
        employeename = request.POST.get('employeename')


        uid=request.session.get('username')
        employee= Employee.objects.get(emp_id=uid)
        empName = employee.fullname
        branch = employee.branchname

        # Save new customer (example)
        new_customer = Customer.objects.create(
            customer_id=new_id,
            name=name,
            mobile=mobile,
            email=email,
            village=village,
            Taluk=Taluk,
            district=district,
            state=state,
            pincode=pincode,
            employeename=empName,
            branchname=branch,
            product=product,


        )

        # Redirect or respond after saving the customer
        return redirect('customer')  # or return some success message

    return render(request, 'Add_customer.html')


def customer_list(request):
    customers = Customer.objects.all()  # Fetch all customers from the database
    return render(request, 'customer_list.html', {'customers': customers})


def edit_customer(request, customer_id):
    # Get the customer by ID or return a 404 if not found
    customer = get_object_or_404(Customer, id=customer_id)

    # Render the edit customer page with the customer data
    return render(request, 'edit_customer.html', {'customer': customer})






def edit_customer(request, id):
    # Get the branch object to edit
    customer = get_object_or_404(Customer, id=id)

    # Handle form submission
    if request.method == 'POST':
        # Manually retrieve and update the branch fields
        customer.name = request.POST.get('name')
        customer.mobile = request.POST.get('mobile')
        customer.Taluk = request.POST.get('Taluk')
        customer.district = request.POST.get('district')
        customer.pincode = request.POST.get('pincode')
        customer.state = request.POST.get('state')
        customer.save()
        return redirect('customer_list')  # Redirect to the branch list after saving

    # Prepopulate form fields for the GET request
    return render(request, 'edit_customer.html', {'customer': customer})



def dealer_create(request, dealer_id=None):
    dealer = None
    if dealer_id:
        dealer = get_object_or_404(Dealer, id=dealer_id)

    if request.method == "POST":
        # Extract form data
        firm_name = request.POST.get("Firm_name")
        owner_name = request.POST.get("Owner_name")
        email = request.POST.get("email")
        village = request.POST.get("village")
        taluk = request.POST.get("Taluk")
        district = request.POST.get("district")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        gst = request.POST.get("gst")
        adhar = request.POST.get("adhar")
        pan = request.POST.get("pan")
        contact=request.POST.get("contact")
        adhar_document = request.FILES.get("adhar_document")
        pan_document = request.FILES.get("pan_document")
        bank_document = request.FILES.get("bank_document")
        gst_doc = request.FILES.get("gst_doc")

        # Create or update dealer instance
        if dealer:
            dealer.Firm_name = firm_name
            dealer.Owner_name = owner_name
            dealer.email = email
            dealer.village = village
            dealer.Taluk = taluk
            dealer.district = district
            dealer.state = state
            dealer.pincode = pincode
            dealer.gst = gst
            dealer.adhar = adhar
            dealer.pan = pan
            dealer.contact = contact
            dealer.adhar_document = adhar_document or dealer.adhar_document
            dealer.pan_document = pan_document or dealer.pan_document
            dealer.bank_document = bank_document or dealer.bank_document
            dealer.gst_doc = gst_doc or dealer.gst_doc
            dealer.save()
        else:
            Dealer.objects.create(
                Firm_name=firm_name,
                Owner_name=owner_name,
                email=email,
                village=village,
                Taluk=taluk,
                district=district,
                state=state,
                pincode=pincode,
                gst=gst,
                adhar=adhar,
                pan=pan,
                adhar_document=adhar_document,
                pan_document=pan_document,
                bank_document=bank_document,
                gst_doc=gst_doc,
                contact=contact,
            )
        return redirect("dealer_list")

    context = {"dealer": dealer}
    return render(request, "dealer.html", context)


# View for listing dealers
def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, "dealer_list.html", {"dealers": dealers})



def edit_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)  # Fetch dealer by ID

    if request.method == "POST":
        # Update dealer fields from form data
        dealer.Firm_name = request.POST.get("Firm_name")
        dealer.Owner_name = request.POST.get("Owner_name")
        dealer.email = request.POST.get("email")
        dealer.village = request.POST.get("village")
        dealer.Taluk = request.POST.get("Taluk")
        dealer.district = request.POST.get("district")
        dealer.state = request.POST.get("state")
        dealer.pincode = request.POST.get("pincode")
        dealer.gst = request.POST.get("gst")
        dealer.adhar = request.POST.get("adhar")
        dealer.pan = request.POST.get("pan")

        # Handle uploaded files (replace only if new file is uploaded)
        if request.FILES.get("adhar_document"):
            dealer.adhar_document = request.FILES.get("adhar_document")
        if request.FILES.get("pan_document"):
            dealer.pan_document = request.FILES.get("pan_document")
        if request.FILES.get("bank_document"):
            dealer.bank_document = request.FILES.get("bank_document")
        if request.FILES.get("gst_doc"):
            dealer.gst_doc = request.FILES.get("gst_doc")

        # Save the updated dealer record
        dealer.save()

        return redirect("dealer_list")  # Redirect to the dealer list page

    return render(request, "dealer_edit.html", {"dealer": dealer})


def admin_dashboard(request):
    print("admin_home view is being called!")  # Debugging point

    # Count of employees in the Users table
    employee_count = Employee.objects.count()

    # Count of customers in the Customer table
    customer_count = Customer.objects.count()

    # Define loan types to track

    branch_count= Branch.objects.count()
    # Debugging the final context
    context = {
        'employee_count': employee_count,
        'customer_count': customer_count,
        'branch_count':branch_count,
    }

    print("Context:", context)  # Debugging point

    return render(request, 'admin_dashboard.html', context)