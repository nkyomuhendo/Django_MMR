from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# New intros for extra security to some views or urls ---- Nico
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddProductForm, ExerciseForm

from .models import Category, Product, Exercise
from .forms import CategoryForm, ProductForm
# from .forms import ExerciseForm

from .utils import create_exercises_from_product

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in!")
            return redirect('webapp-home')
        else:
            messages.success(request, "There was an error logging in, Please try again!...")
            return redirect('webapp-home')
    else:
         return render(request, 'webapp/home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out ...")
    return redirect('webapp-home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Succesfully Registered! Welcome ... ")
            return redirect('webapp-home')       
    else:
        form = SignUpForm()
        
    return render(request, 'webapp/register.html', {'form':form})

@login_required
def category_list(request):

    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'webapp/category_create.html', context)

# # products_view
@login_required
def products_view(request):

    context = {
        # 'products': Product.objects.all()
        'products': Product.objects.filter(created_by=request.user)
    }

    return render(request, 'webapp/products_view.html', context)

# exercise_view
@login_required
def exercise_view(request):
    
    context = {
        'exercises': Exercise.objects.all()
        
    }

    return render(request, 'webapp/exercises_view.html', context)

# Products_view revised and improved

# @login_required
# def product_view(request, pk):
#     if request.user.is_authenticated:
#         try:
#             # Lookup product record
#             product = get_object_or_404(Product, id=pk, created_by=request.user)
#             product_records = Exercise.objects.filter(product=product)

#             # Initialize Opn_Sym with a default value
#             Opn_Sym = ''

#             if product.category == "Addition":
#                 Opn_Sym = '+'
#             elif product.category == "Multiplication":
#                 Opn_Sym = 'X'
#             elif product.category == "Subtraction":
#                 Opn_Sym = '-'
#             elif product.category == "Division":
#                 Opn_Sym = '/'

#             print(f"Operation: {product.category} Type: {type(product.category)}")
#             print(f"Operation: {Opn_Sym} Type: {type(Opn_Sym)}")
            
#             return render(request, 'webapp/product.html', {'product_records': product_records, 'Opn_Sym': Opn_Sym})
#         except Product.DoesNotExist:
#             messages.error(request, "Product does not exist.")
#             return redirect('webapp-home')
#     else: 
#         messages.success(request, "Sorry, you must be logged in to view this page.")
#         return redirect('webapp-home')

# product yet improved version 3

@login_required
def product_view(request, pk):
    if request.user.is_authenticated:
        try:
            # Lookup product record
            product = get_object_or_404(Product, id=pk, created_by=request.user)
            product_records = Exercise.objects.filter(product=product)

            # Initialize Opn_Sym with a default value
            Opn_Sym = ''

            # Assuming product.category is an object and it has a 'name' attribute
            category_name = product.category.name

            if category_name == "Addition":
                Opn_Sym = '+'
            elif category_name == "Multiplication":
                Opn_Sym = 'X'
            elif category_name == "Subtraction":
                Opn_Sym = '-'
            elif category_name == "Division":
                Opn_Sym = '/'

            print(f"Operation: {category_name} Type: {type(category_name)}")
            print(f"Operation: {Opn_Sym} Type: {type(Opn_Sym)}")
            
            return render(request, 'webapp/product.html', {'product_records': product_records, 'Opn_Sym': Opn_Sym})
        except Product.DoesNotExist:
            messages.error(request, "Product does not exist.")
            return redirect('webapp-home')
    else: 
        messages.success(request, "Sorry, you must be logged in to view this page.")
        return redirect('webapp-home')


@login_required
def exercise_views(request, pk):
    product = Product.objects.get(id=pk, created_by=request.user)
    context = {
        # 'exercises': Exercise.objects.all().filter(id=pk)
        'exercises': Exercise.objects.filter(product=product)
    }

    return render(request, 'webapp/exercises_view.html', context)

# @login_required
# def product_view(request, pk):
#     if request.user.is_authenticated:
#         # Lookup product record
#         # product_record = Exercise.objects.all().filter(product=pk)
#         product = Product.objects.get(id=pk, created_by=request.user)
#         # print("Product Object: ", product.category)
#         product_record = Exercise.objects.filter(product=product)
#         # print("Product Object: ", product_record.category)
#         # product_record = Exercise.objects.all()
#         operation = product.category
#         if (operation == "Addition"):
#             Opn_Sym = '+'
#         elif (operation == "Multiplication"):
#             Opn_Sym = 'X'
#         elif (operation == "Subtraction"):
#             Opn_Sym = '-'
#         elif (operation == "Division"):
#             Opn_Sym = '/'

#         print(f"Operation:  {operation} Type: { type(operation)}")
#         print(f"Operation:  {Opn_Sym} Type: { type(Opn_Sym)}")
#         return render(request, 'webapp/product.html', {'product_record': product_record})
#     else: 
#         messages.success(request, "Sorry You must be logged in to view this page...!")
#         return redirect('webapp-home')

def add_product(request):
    created_by=request.user
    print(created_by)
    form = AddProductForm(request.POST or None)
    if request.user.is_authenticated:
        created_by = request.user
        if request.method == 'POST':
            # print("Verified Post method used!")
            if form.is_valid():
                form.save()
                # add_product = form.save()
                # add_record = form.save()
                messages.success(request, "Product Added...")
                return redirect('webapp-home')
            else:
                return render(request, 'webapp/add_product.html', {'form': form})
                # return render(request, 'record_new_deal.html', {'form': form})

        return render(request, 'webapp/add_product.html', {'form': form})
    else:
        messages.success(request, "You must Be Logged In...")
        return redirect('webapp-home')
    
    # your_app/views.py

# from django.shortcuts import render, redirect
# from .forms import ExerciseForm

def create_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_exercise')  # Redirect to a success page or wherever you want
    else:
        form = ExerciseForm()
    
    return render(request, 'webapp/create_exercise.html', {'form': form})


# your_app/views.py

# from django.shortcuts import render, redirect
# from .forms import CategoryForm, ProductForm

# @login_required
# def create_category(request):
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category_list')  # Redirect to a category list page or wherever you want
#     else:
#         form = CategoryForm()
    
#     return render(request, 'webapp/create_category.html', {'form': form})

# Presenting below improved category create view v2:


# Decorator to check if the user is a staff member (admin)
def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to a category list page or wherever you want
    else:
        form = CategoryForm()
    
    return render(request, 'webapp/create_category.html', {'form': form})


@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user  # Assuming you have authentication in place
            product.save()
            create_exercises_from_product(product, request.user)
            return redirect('products-view')  # Redirect to a product list page or wherever you want
    else:
        form = ProductForm()
    
    return render(request, 'webapp/create_product.html', {'form': form})


# from django.shortcuts import render, redirect
# from .forms import ProductForm
# from .utils import create_exercises_from_product

# def create_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.created_by = request.user
#             product.save()
#             create_exercises_from_product(product, request.user)
#             return redirect('product_list')  # Redirect to a product list page or wherever you want
#     else:
#         form = ProductForm()
    
#     return render(request, 'create_product.html', {'form': form})


