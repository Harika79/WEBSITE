from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import  News
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def web_page6(request):
    return render(request, 'web_page6.html')

@login_required
def learn(request):
    return render(request, 'learn.html')
@login_required
def web_page4(request):
    return render(request, 'web_page4.html')
@login_required
def web_page5(request):
    return render(request, 'web_page5.html')
@login_required
def web_page1(request):
    return render(request, 'web_page1.html')
@login_required
def web_page2(request):
    return render(request, 'web_page2.html')
@login_required
def web_page3(request):
    return render(request, 'web_page3.html')
@login_required
def news(request):
    if request.method=="POST":
       title=request.POST['title']
       author = request.POST['author']
       date = request.POST['date']
       content = request.POST['content']
       india = News(title, author, date, content)
       india.save()
    return render(request, 'user_content.html')
@login_required
def show_news(request):
    # Retrieve all news objects from the database
    news_objects = News.objects.all()

    # Render the HTML template with the news data
    return render(request, 'show_content.html', {'data': news_objects})
@login_required
def page0(request):
    return render(request, 'page0.html')
@login_required
def page2(request):
    return render(request, 'page2.html')
@login_required
def page3(request):
    return render(request, 'page3.html')
@login_required
def page4(request):
    return render(request, 'page4.html')
@login_required
def page5(request):
    return render(request, 'page5.html')












# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# from .forms import UserRegistrationForm  # Import the UserRegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts/login')
#     else:
#         form = UserRegistrationForm()
    
#     # Print the form fields to check if the email field is present
#     print(form.fields)

#     # Pass the form instance to the template context
#     return render(request, 'register.html', {'form': form})
# def user_login(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('http://127.0.0.1:8000/home/')
#         else:
#             messages.info(request, 'username Or password is incorrect')
#             # return render(request, 'accounts/login.html', context)

#     context={}
#     return render(request, 'login.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('http://127.0.0.1:8000/home/')  # Redirect to the home page after successful login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# views.py
from django.shortcuts import render, redirect
from .models import Book, PurchaseDetail
@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        image = request.FILES.get('image')  # Retrieve uploaded image file
        pdf_file = request.FILES.get('pdf_file')  # Retrieve uploaded PDF file
        email = request.POST.get('email')  # Retrieve email
        
        # Create the book object
        book = Book(title=title, author=author, price=price, image=image, email=email)
        
        # If a PDF file is provided, save it to the book object
        if pdf_file:
            book.pdf_file = pdf_file
        
        # Save the book object to the database
        book.save()
        
        return redirect('show_books')
    
    return render(request, 'add_book.html')
# def add_book(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         author = request.POST['author']
#         price = request.POST['price']
#         image = request.FILES.get('image')  # Retrieve uploaded image file
#         url = request.POST.get('url')  # Retrieve URL
#         Book.objects.create(title=title, author=author, price=price, image=image, url=url)
#         return redirect('show_books')
#     return render(request, 'add_book.html')
@login_required
def show_books(request):
    books = Book.objects.all()
    purchased_books = PurchaseDetail.objects.filter(book__in=books, user=request.user).values_list('book_id', flat=True)
    return render(request, 'show_books.html', {'books': books, 'purchased_books': purchased_books})
# def show_books(request):
#     books = Book.objects.all()
#     return render(request, 'show_books.html', {'books': books})
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, PurchaseDetail
from django.core.mail import send_mail
@login_required
def purchase_book(request, book_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        book = Book.objects.get(id=book_id)
        credit_card = request.POST.get('credit_card')
        timestamp=request.POST.get('timestamp')
        PurchaseDetail.objects.create(name=name, email=email, address=address, book=book, user=request.user, timestamp=timestamp,credit_card=credit_card)
        return redirect('show_purchase_details')
    return render(request, 'purchase_book.html')
@login_required
def show_purchase_details(request):
    # Get the latest purchase detail
    latest_purchase = PurchaseDetail.objects.order_by('-timestamp').first()

    # Check if a purchase detail exists
    if latest_purchase:
        # Retrieve the associated book
        book = latest_purchase.book

        # Send email notification to the buyer using the email address from the PurchaseDetail model
        subject = f'Your e-book {book.title} has been purchased'
        message = f'Dear {latest_purchase.name},\n\nThank you for purchasing the book "{book.title}". You can now access this e-book from our website.\n\nKeep Reading our books:)\nBest regards,\nFrom space technology e-bookstore'
        sender_email = 'your_bookstore@example.com'  # Update with your sender email address
        send_mail(subject, message, sender_email, [latest_purchase.email])

    # Fetch all purchase details (optional)
    purchase_details = PurchaseDetail.objects.order_by('-timestamp')[0:1]

    return render(request, 'show_purchase_details.html', {'purchase_details': purchase_details})

# def show_purchase_details(request):
#     # Get the latest purchase detail
#     latest_purchase = PurchaseDetail.objects.order_by('-timestamp').first()

#     # Check if a purchase detail exists
#     if latest_purchase:
#         # Retrieve the associated book
#         book = latest_purchase.book

#         # Send email notification to the buyer using the email address from the Book model
#         subject = f'Your book {book.title} has been purchased'
#         message = f'Dear {book.email},\n\nThank you for purchasing the book "{book.title}". It will be delivered to the following address:\n\n{latest_purchase.address}\n\nBest regards,\nYour Bookstore'
#         sender_email = 'your_bookstore@example.com'  # Update with your sender email address
#         send_mail(subject, message, sender_email, [book.email])

#     # Fetch all purchase details (optional)
#     purchase_details = PurchaseDetail.objects.order_by('-timestamp')[0:1]

#     return render(request, 'show_purchase_details.html', {'purchase_details': purchase_details})
# def show_purchase_details(request):
#     purchase_details = PurchaseDetail.objects.order_by('-timestamp')[0:1]
#     return render(request, 'show_purchase_details.html', {'purchase_details': purchase_details})
# def show_purchase_details(request):
#     purchase_details = PurchaseDetail.objects.all()
#     return render(request, 'show_purchase_details.html', {'purchase_details': purchase_details})
@login_required
def show_purchased_books(request):
    if request.user.is_authenticated:
        purchased_books = PurchaseDetail.objects.filter(user=request.user)
        return render(request, 'show_purchased_books.html', {'purchased_books': purchased_books})
    else:
        return redirect('login')
    
@login_required
def books(request):
    return render(request, 'books.html')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import PurchaseDetail

# Restrict access to superusers only
def superuser_required(function):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url='/login/',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

@superuser_required
def show_all_purchase_details(request):
    all_purchase_details = PurchaseDetail.objects.select_related('user', 'book').order_by('-timestamp')
    return render(request, 'show_all_purchase_details.html', {'all_purchase_details': all_purchase_details})

@superuser_required
def delete_purchase_detail(request, purchase_detail_id):
    purchase_detail = get_object_or_404(PurchaseDetail, pk=purchase_detail_id)
    if request.method == 'POST':
        purchase_detail.delete()
        messages.success(request, 'Purchase detail deleted successfully.')
        return redirect('show_all_purchase_details')
    return render(request, 'confirm_delete_purchase_detail.html', {'purchase_detail': purchase_detail})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            # return redirect('show_all_purchase_details')
            return redirect('project_list')
            # return redirect('accounts/profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin_login.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def delete_book(request, book_id):
    # Retrieve the book object to be deleted
    book = get_object_or_404(Book, id=book_id)
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Delete the book
        book.delete()
        # Redirect to a success page or another appropriate page
        return redirect('show_books')  # Redirect to the book list page
    
@superuser_required
def admin_learn(request):
    return render(request,'admin_learn.html')
