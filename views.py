import decimal
import json
from _pydecimal import Decimal

from django.core.exceptions import ValidationError
from django.db.models import Max, Sum
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from mahalaxmi_app.models import Login ,Branch ,Customer, Dealer, Item,BookingItem, Stock,CustomerBalance,Transfer,Subsidy,Employee_register
from pyexpat.errors import messages
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request,"index.html")
import logging

logger = logging.getLogger(__name__)
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        password = request.POST.get('t2')

        logger.debug(f"Attempting login for username: {username}")

        # Check if the user exists
        udata = Login.objects.filter(username=username).first()

        if udata:
            logger.debug(f"User found: {udata.username}")
            if password == udata.password:
                request.session['utype'] = udata.utype
                logger.debug(f"Password correct for user: {udata.username}")

                # Check for employee type and fetch employee details
                if udata.utype == 'employee':
                    employee = Emp.objects.filter(employee_id=username).first()
                    if employee:
                        request.session['employee_name'] = employee.employee_name
                        request.session['employee_id'] = employee.employee_id  # Save employee ID
                        logger.debug(f"Employee name set to: {employee.employee_name}")

                # Redirect based on user type
                if udata.utype in ['user', 'admin']:
                    return render(request, 'index.html')
                elif udata.utype == 'employee':
                    return redirect('emp_home')
                elif udata.utype == 'superadmin':
                    return render(request, 'superadmin.html')
            else:
                logger.warning(f"Invalid password for user: {username}")
                return render(request, 'userlogin.html', {'msg': 'Invalid Password'})
        else:
            logger.warning(f"User not found: {username}")
            return render(request, 'userlogin.html', {'msg': 'Invalid Username'})

    return render(request, 'userlogin.html')

def emp_home(request):
    employee_name = request.session.get('employee_name', 'Employee')  # Default to 'Employee' if not found
    return render(request, 'Employee/emp_home.html', {'employee_name': employee_name})

def branch(request):
    if request.method == 'POST':
        branchname = request.POST.get('branchname')
        village = request.POST.get('village')
        Taluk = request.POST.get('Taluk')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')

        if branchname:
            Branch.objects.create(branchname=branchname, village=village ,Taluk=Taluk, district=district,pincode=pincode)

            return redirect('branch')  # Redirect to the same page or a success page

        messages.error(request, 'Please fill in all fields.')

    return render(request, 'Branch/branch.html')


def branch_view(request):
    # Fetch all branch details
    branches = Branch.objects.all()

    # Render the template and pass the branch data
    return render(request, 'Branch/branch_view.html', {'branches': branches})

def generate_employee_id():
    # Fetch the last employee_id (max value) from the Employee model
    last_employee = Employee_register.objects.aggregate(max_id=Max('employee_id'))
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

from django.contrib import messages
from django.http import JsonResponse
def employee_reg(request):
    branches = Branch.objects.all()

    if request.method == 'POST':
        employee_id = generate_employee_id()
        employee_name = request.POST.get('employee_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        village = request.POST.get('village')
        taluk = request.POST.get('taluk')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        nationality = request.POST.get('nationality')
        contact = request.POST.get('contact')
        state = request.POST.get('state')
        marital_status = request.POST.get('marital_status')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        parent_mobile = request.POST.get('parent_mobile')
        occupation = request.POST.get('occupation')
        previous_company = request.POST.get('previous_company')
        work_start_date = request.POST.get('work_start_date')
        work_end_date = request.POST.get('work_end_date')
        reason_leaving = request.POST.get('reason_leaving')
        branch_id = request.POST.get('branch')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        doj = request.POST.get('doj')
        tenth_qualification = request.POST.get('tenth_qualification')
        tenth_passout_year = request.POST.get('tenth_passout_year')
        tenth_percentage = request.POST.get('tenth_percentage')
        twelfth_qualification = request.POST.get('twelfth_qualification')
        twelfth_passout_year = request.POST.get('twelfth_passout_year')
        twelfth_percentage = request.POST.get('twelfth_percentage')
        degree_qualification = request.POST.get('degree_qualification')
        degree_passout_year = request.POST.get('degree_passout_year')
        degree_percentage = request.POST.get('degree_percentage')
        role = request.POST.get('role')
        jobrole = request.POST.get('jobrole')
        pf = request.POST.get('pf')
        esic = request.POST.get('esic')
        adhar = request.POST.get('adhar')
        sallery = request.POST.get('sallery')
        pan = request.POST.get('pan')




        # Handle file uploads
        aadhaar_document = request.FILES.get('aadhaar_document')
        pancard = request.FILES.get('pancard')
        bank_document = request.FILES.get('bank_document')
        passport_size_photo = request.FILES.get('passport_size_photo')
        experienceletter = request.FILES.get('experienceletter')

        # Basic validation
        if not employee_name or not email or not password or not branch_id:
            messages.error(request, 'All fields are required.')
            return render(request, 'Employee/Employee_reg.html', {'branches': branches})

        if Employee_register.objects.filter(contact=contact).exists():
            messages.error(request, 'This contact number is already registered.')
            return render(request, 'Employee/Employee_reg.html', {'branches': branches})

        try:
            branch = Branch.objects.get(id=branch_id)

            # Create and save the employee
            employee = Employee_register(
                employee_id=employee_id,
                employee_name=employee_name,
                gender=gender,
                email=email,
                password=password,  # Remember to hash the password in production
                nationality=nationality,
                branchname=branch.branchname,
                village=village,
                taluk=taluk,
                district=district,
                pincode=pincode,
                contact=contact,
                state=state,
                marital_status=marital_status,
                father_name=father_name,
                mother_name=mother_name,
                parent_mobile=parent_mobile,
                occupation=occupation,
                previous_company=previous_company,
                work_start_date=work_start_date,
                work_end_date=work_end_date,
                aadhaar_document=aadhaar_document,
                reason_leaving=reason_leaving,
                pancard=pancard,
                bank_document=bank_document,
                passport_size_photo=passport_size_photo,
                dob=dob,
                age=age,
                doj=doj,
                tenth_qualification=tenth_qualification,
                tenth_passout_year=tenth_passout_year,
                tenth_percentage=tenth_percentage,
                twelfth_qualification=twelfth_qualification,
                twelfth_passout_year=twelfth_passout_year,
                twelfth_percentage=twelfth_percentage,
                degree_qualification=degree_qualification,
                degree_passout_year=degree_passout_year,
                degree_percentage=degree_percentage,
                role=role,
                jobrole=jobrole,
                pf=pf,
                esic=esic,
                sallery=sallery,
                adhar=adhar,
                pan=pan,
                experienceletter=experienceletter,


            )

            employee.save()

            # Create login record
            Login.objects.create(utype='employee', username=employee_id, password=password)

            messages.success(request, 'Employee registered successfully.')
            return redirect('employee_view')

        except Branch.DoesNotExist:
            messages.error(request, 'Selected branch does not exist.')
            return render(request, 'Employee/Employee_reg.html', {'branches': branches})
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'Employee/Employee_reg.html', {'branches': branches})

    # Default return for GET requests
    return render(request, 'Employee/Employee_reg.html', {'branches': branches})


def employee_certificate(request, employee_id):
    # Fetch the employee instance based on employee_id
    employee = get_object_or_404(Employee_register, employee_id=employee_id)

    # Render the template with the employee data
    return render(request, 'employee_certificate.html', {'employee': employee})

def check_duplicate_contact(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        exists = Employee_register.objects.filter(contact=contact).exists()  # Adjust model name as needed
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False}, status=400)
def employee_view(request):
    if request.method == 'POST':
        # Handle form submission and create a new employee
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        branchname = request.POST.get('branchname')

        # Create and save the new employee
        Employee_register.objects.create(
            employee_id=employee_id,
            name=name,
            email=email,
            password=password,
            address=address,
            branchname=branchname
        )
        return redirect('Employee/employee_view')  # Redirect to avoid form resubmission

    # Fetch all employees to display in the template
    employees = Employee_register.objects.all()

    return render(request, 'Employee/employee_view.html', {'employees': employees})


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee_register, pk=employee_id)

    if request.method == 'POST':
        employee.fullname = request.POST.get('fullname')
        employee.fullname = request.POST.get('fullname')
        employee.dob = request.POST.get('dob')
        employee.gender = request.POST.get('gender')
        employee.contact = request.POST.get('contact')
        employee.email = request.POST.get('email')
        employee.nationality = request.POST.get('nationality')
        employee.city = request.POST.get('city')
        employee.state = request.POST.get('state')
        employee.pincode = request.POST.get('pincode')
        employee.district = request.POST.get('district')
        employee.Taluk = request.POST.get('Taluk')
        employee.adhar = request.POST.get('adhar')
        employee.pancard = request.POST.get('pancard')
        employee.fathername = request.POST.get('fathername')
        employee.mothername = request.POST.get('mothername')
        employee.occupation = request.POST.get('occupation')
        employee.previoucompany = request.POST.get('previoucompany')
        employee.role = request.POST.get('role')
        employee.start_date = request.POST.get('start_date')
        employee.end_date = request.POST.get('end_date')
        employee.jrole = request.POST.get('jrole')
        employee.doj = request.POST.get('doj')
        employee.pf = request.POST.get('pf')
        employee.esic = request.POST.get('esic')
        employee.salary = request.POST.get('salary')


        employee.save()
        return redirect('employee_view')

    return render(request, 'Employee/edit_employee.html', {'employee': employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee_register, pk=employee_id)
    employee.delete()
    return redirect('employee_view')

def customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        branch_id = request.POST.get('branchname')
        employee_id = request.POST.get('employeename')
        village = request.POST.get('village')
        Taluk = request.POST.get('Taluk')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        product = request.POST.get('product')

        # Basic validation
        if not name or not mobile or not branch_id or not employee_id:
            messages.error(request, 'All fields are required.')
            return render(request, 'customer/customer.html', {'branches': Branch.objects.all(), 'employees': Employee.objects.all()})

        # Generate new customer_id
        last_customer = Customer.objects.order_by('customer_id').last()
        if last_customer is not None:
            new_id = last_customer.customer_id + 1
        else:
            new_id = 1  # Start from 1 if no customer exists

        # Create and save the customer
        customer = Customer(
            customer_id=new_id,
            name=name,
            mobile=mobile,
            email=email,  # Remember to hash in production
            branchname=branch_id,
            employeename=employee_id,
            village=village,
            Taluk=Taluk,
            district=district,
            pincode=pincode,
            product=product,
        )
        customer.save()

        return redirect('customer_view')  # Redirect to success page or index

    return render(request, 'customer/customer.html', {'branches': Branch.objects.all(), 'employees': Employee.objects.all()})

def check_mobile(request):
    mobile = request.GET.get('mobile')
    exists = Customer.objects.filter(mobile=mobile).exists()
    return JsonResponse({'exists': exists})

def customer_view(request):
    customers = Customer.objects.all()  # Retrieve all customer records
    return render(request, 'Customer/customer_view.html', {'customers': customers})


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.mobile = request.POST.get('mobile')
        customer.address = request.POST.get('address')
        customer.email = request.POST.get('email')
        customer.branchname = request.POST.get('branchname')
        customer.employeename = request.POST.get('employeename')
        customer.save()
        return redirect('customer_view')  # Redirect to the customer list after saving
    return render(request, 'customer/edit_customer.html', {'customer': customer})

def remove_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customer_view')

def add_dealer(request):
    if request.method == 'POST':
        dealer_name = request.POST.get('dealer_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        document = request.POST.get('document')
        village = request.POST.get('village')
        Taluk = request.POST.get('Taluk')
        district = request.POST.get('district')
        product = request.POST.get('product')
        gst = request.POST.get('gst')
        pincode = request.POST.get('pincode')
        # Get the selected branch ID from the form

        # Create a new dealer
        Dealer.objects.create(
            dealer_name=dealer_name,
            mobile=mobile,
            email=email,
            document=document,# Remember to hash this in production
            village=village,
            Taluk=Taluk,
            district=district,
            product=product,
            gst=gst,
            pincode=pincode,
            # Use the branch ID to set the foreign key
        )
        return redirect('dealer_view')  # Redirect to a success page

    branches = Branch.objects.all()  # Get all branches to display in the form
    return render(request, 'Employee/add_dealer.html', {'branches': branches})

def dealer_view(request):
    dealers = Dealer.objects.all()
    return render(request, 'Employee/dealer_view.html', {'dealers': dealers})
def edit_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    if request.method == 'POST':
        dealer.dealer_name = request.POST['dealer_name']
        dealer.mobile = request.POST['mobile']
        dealer.email = request.POST['email']
        dealer.document = request.POST['document']
        dealer.village = request.POST['village']
        dealer.Taluk = request.POST['Taluk']
        dealer.district = request.POST['district']
        dealer.product = request.POST['product']
        dealer.gst = request.POST['gst']
        dealer.gst = request.POST['pincode']
        dealer.save()
        return redirect('dealer_view')

    return render(request, 'Employee/edit_dealer.html', {'dealer': dealer})
def remove_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    dealer.delete()
    return redirect('dealer_view')

def add_item(request):
    if request.method == 'POST':
        Itemname = request.POST.get('Itemname')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        part_no = request.POST.get('part_no')
        description = request.POST.get('description')
        dispatch = request.POST.get('dispatch')
        branch_id = request.POST.get('branchname')

        # Create a new item in the Item model
        item = Item.objects.create(
            Itemname=Itemname,
            qty=qty,
            price=price,
            part_no=part_no,
            description=description,
            dispatch=dispatch,
            branchname=branch_id
        )

        # Create a new entry in the Stock model
        stock = Stock.objects.create(
            Itemname=Itemname,
            qty=qty,
            price=price,
            part_no=part_no,
            description=description,
            dispatch=dispatch,
            branchname=branch_id
        )

        return redirect('item_view')  # Redirect to item list page

    branches = Branch.objects.all()  # Get all branches to display in the form
    return render(request, 'Employee/add_item.html', {'branches': branches})

def item_view(request):
    items = Stock.objects.all()
    transfer_success = None

    if request.method == 'POST':
        item_name = request.POST.get('itemname')
        source_branch = request.POST.get('source_branch')
        destination_branch = request.POST.get('destination_branch')
        transfer_qty = int(request.POST.get('transfer_qty'))

        # Fetch the stock item for the source branch
        source_stock = Stock.objects.get(Itemname=item_name, branchname=source_branch)

        # Check if sufficient quantity is available
        if source_stock.qty >= transfer_qty:
            # Reduce stock from source branch
            source_stock.qty -= transfer_qty
            source_stock.save()

            # Check if the destination branch already has the item
            destination_stock, created = Stock.objects.get_or_create(Itemname=item_name, branchname=destination_branch)

            # Increase stock in destination branch
            destination_stock.qty += transfer_qty
            destination_stock.save()

            transfer_success = f"Successfully transferred {transfer_qty} of {item_name} from {source_branch} to {destination_branch}."
        else:
            transfer_success = "Insufficient stock in the source branch."

    return render(request, 'Employee/item_view.html', {'items': items, 'transfer_success': transfer_success})

 # Adjust to your view name
def edit_item(request, item_id):
    # Fetch the item by ID or return 404 if not found
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        # Get data from POST request and update the item fields
        item.Itemname = request.POST.get('itemname')
        item.qty = request.POST.get('qty')
        item.price = request.POST.get('price')
        item.part_no = request.POST.get('part_no')
        item.description = request.POST.get('description')
        item.dispatch = request.POST.get('dispatch')
        # Save the updated item
        item.save()
        # Redirect to the item list or any other relevant page
        return redirect('item_view')  # Assuming you have a list view for items

    # Render the edit form template with current item data
    return render(request, 'Employee/edit_item.html', {'item': item})


def Item_view_stock(request):
    items = Item.objects.all()
    query_itemname = request.GET.get('itemname')
    query_branchname = request.GET.get('branchname')

    if query_itemname:
        items = items.filter(Itemname__icontains=query_itemname)

    if query_branchname:
        items = items.filter(branchname__icontains=query_branchname)  # Ensure this field exists in your model

    return render(request, 'Employee/Item_view_stock.html', {'items': items})










def customer_booking(request):
    if request.method == "POST":
        customername = request.POST.get('customername')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        branchname = request.POST.get('branchname')
        village = request.POST.get('village')
        Taluk = request.POST.get('Taluk')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        totalamount = request.POST.get('totalamount')
        itemname = request.POST.get('itemname')
        quantity=request.POST.get('quantity')
        price = request.POST.get('price')
        totalAmount = request.POST.get('totalAmount')
        customer_id = request.POST.get('customer_id')

        customer = Customer.objects.get(id=customer_id)

        BookingItem.objects.create(
            customername=customername,
            mobile=mobile,
            email=email,
            branchname=branchname,
            village=village,
            Taluk=Taluk,
            district=district,
            pincode=pincode,
            totalamount=totalamount,
            itemname=itemname,
            quantity=quantity,
            price=price,
            totalAmount=totalAmount,
            customer_id=customer.customer_id,

            # Updated to reflect the actual field
        )

        return redirect('customer_booking')

    customers = Customer.objects.all()
    items = Item.objects.all()
    return render(request, 'customer/customer_booking.html', {'customers': customers, 'items': items})
def get_customer_details(request):
    name = request.GET.get('name', None)
    if name:
        try:
            customer = Customer.objects.get(name=name)
            data = {
                'mobile': customer.mobile,
                'email': customer.email,
                'branchname': customer.branchname,
                'village': customer.village,
                'Taluk': customer.Taluk,
                'district': customer.district,
                'pincode': customer.pincode,
                'customer_id': customer.id,
            }
            return JsonResponse(data)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_item_details(request):
    item_name = request.GET.get('item_name')
    if item_name:
        items = Item.objects.filter(Itemname=item_name)
        if items.exists():
            item = items.first()  # Get the first item
            data = {
                'qty': item.qty,
                'price': float(item.price),
                'part_no': item.part_no,
                'description': item.description,
                'dispatch': item.dispatch,
                'branchname': item.branchname,
            }
            return JsonResponse(data)
        return JsonResponse({'error': 'Item not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)









def customer_booking_view(request):
    customername = request.GET.get('customername')  # Get customer name from the query parameters
    if customername:
        bookings = BookingItem.objects.filter(customername=customername)
    else:
        bookings = BookingItem.objects.all()  # Show all if no customer name is provided

    return render(request, 'customer/customer_booking_view.html', {'bookings': bookings})
def customer_balance(request):
    customers = BookingItem.objects.values('customername').distinct()  # Get distinct customer names
    return render(request, 'customer/customer_balance.html', {'customers': customers})

def save_customer_balance(request):
    if request.method == 'POST':
        customername = request.POST['customername']  # Use square brackets here
        entry_amount = request.POST['entry_amount']
        paymentMode = request.POST['paymentMode']
        pay_status = request.POST['pay_status']
        accountholder = request.POST['accountholder']
        accountnumber = request.POST['accountnumber']
        upiId = request.POST['upiId']
        transactionId = request.POST['transactionId']

        # Save to the database
        CustomerBalance.objects.create(
            customername=customername,
            entry_amount=entry_amount,
            paymentMode=paymentMode,
            pay_status=pay_status,
            accountholder=accountholder,
            accountnumber=accountnumber,
            upi_id=upiId,
            transaction_id=transactionId
        )

        return redirect('customer_balance')  # Redirect after saving
    return render(request, 'customer/customer_balance.html')
# Handle AJAX request for fetching items based on customer selection
def get_customer_items(request):
    customername = request.GET.get('customername')
    booking_items = BookingItem.objects.filter(customername=customername)

    data = []
    for i, item in enumerate(booking_items, 1):
        data.append({
            'si_no': i,
            'itemname': item.itemname,
            'totalAmount': item.totalAmount,
        })

    return JsonResponse({'data': data})


def receipt(request, receipt: str):
    # Fetch the booking details for the given receipt number
    customers = CustomerBalance.objects.filter(receipt_number=receipt)

    # Check if any bookings exist for the given receipt number
    if not customers.exists():
        return render(request, 'customer/receipt.html', {'error': 'No bookings found for this receipt.'})

    # Get the first customer for display
    customer = customers.first()

    # Render the receipt template with customer data
    return render(request, 'customer/receipt.html', {'customer': customer})

def get_items_by_branch(request):
    if request.method == 'GET':
        branch_name = request.GET.get('branchname')
        items = Item.objects.filter(branchname=branch_name).values('Itemname', 'qty', 'price')
        item_list = list(items)  # Convert QuerySet to list of dictionaries
        return JsonResponse(item_list, safe=False)





def transfer_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemid')
        branch_to = request.POST.get('branch')
        qty = int(request.POST.get('qty'))

        # Fetch the item
        item = Item.objects.get(id=item_id)
        if item.qty >= qty:
            item.qty -= qty  # Decrease the quantity
            item.save()

            # Create a transfer record, saving the 'from' branch
            transfer = Transfer.objects.create(item=item, branch_from=item.branchname, branch_to=branch_to, qty=qty)

            return JsonResponse({
                'success': True,
                'si_no': transfer.id,  # Assuming 'id' is the serial number
                'itemname': item.Itemname,
                'qty': transfer.qty,
                'price': item.price
            })
        else:
            return JsonResponse({'success': False, 'error': 'Insufficient quantity'})

    # For GET request or other methods
    items = Item.objects.all()
    query_itemname = request.GET.get('itemname')
    query_branchname = request.GET.get('branchname')

    if query_itemname:
        items = items.filter(Itemname__icontains=query_itemname)

    if query_branchname:
        items = items.filter(branchname__icontains=query_branchname)

    branches = Branch.objects.all()  # Fetch all branches
    transfers = Transfer.objects.all()  # Fetch all transfers to display

    return render(request, 'Employee/transfer_item.html', {
        'items': items,
        'branches': branches,
        'transfers': transfers
    })


def get_total_amount(request):
    customer_name = request.GET.get('customer_name')
    if customer_name:
        total_amount = BookingItem.objects.filter(customername=customer_name).aggregate(Sum('totalAmount'))['totalAmount__sum']
        branch_name = BookingItem.objects.filter(customername=customer_name).values('branchname').first()

        return JsonResponse({
            'total_amount': total_amount,
            'branch_name': branch_name['branchname'] if branch_name else None
        })
    return JsonResponse({'total_amount': None, 'branch_name': None})

def sale(request):
    customers = Customer.objects.all()
    return render(request, 'sale.html', {'customers': customers})