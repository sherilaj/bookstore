from django.contrib import messages
from django.shortcuts import redirect, render
from . models import Book, Category, BookRating, Author
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.models import User
from . forms import MessageForm
# Create your views here.

def index(request):
    book = Book.objects.all()
    cat =Category.objects.all()
    return render(request,'index.html',{'book':book,'category':cat})

def getBooks(request):
    book = Book.objects.all()
    return render(request,'book.html',{'book':book})

def detail(request,BookId):
    books =  Book.objects.get(BookId=BookId)
    rating = BookRating.objects.filter(Books=books)
    return render(request,'detail.html',{'book':books,'rating':rating})

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pwd']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('bookapp:login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = User.objects.create_user(first_name=firstname,last_name=lastname,
                                        username=username,email=email,
                                        password=password)
        user.save()
        print("user created")
        return redirect('bookapp:login')
    return render(request,'register.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/')

def trending(request):
    trend = BookRating.objects.filter(Rating__gt=4)
    books = [rating.Books for rating in trend]  # Retrieve associated Book objects
    return render(request, 'trending.html', {'trending': trend, 'books': books})

def MegaDiscount(request):
    dis = Book.objects.filter(DiscountPercent__gt=35)
    return render(request, 'megaDiscount.html', {'discount': dis})

def MessageAddView(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bookapp:index')
    else:
        form = MessageForm()
    return render(request, 'message.html', {'form': form})

def booksByCategory(request,CategoryId):
    cat = Category.objects.get(CategoryId=CategoryId)
    book = Book.objects.filter(Categories=cat)
    return render(request,"category.html",{'books':book,'category':cat})

def booksByAuthor(request,AuthorId):
    aut = Author.objects.get(AuthorId=AuthorId)
    books = Book.objects.filter(Authors=aut)
    context={
        'author':aut,
        'books':books
    }
    return render(request, 'authorBooks.html', context)


def authorList(request):
    author = Author.objects.all()
    return render(request,'author.html',{'author':author})

# def search(request):
#     if 'q' in request.GET:
#         print(request.GET)
#         query = request.GET['q']
#         # Perform case-insensitive search by concatenating multiple filters
#         books = Book.objects.filter(SEOKeyword__icontains=query) | Book.objects.filter(SEOTitle__icontains=query)
#         return render(request, 'searchResults.html', {'books': books, 'query': query})
#     else:
#         return render(request, 'searchResults.html', {})
def search(request):
    query = request.GET.get('q')
    books = None
    if query:
        q_object  = Q(SEOTitle__icontains=query)|Q(SEOKeyword__icontains=query)
        books = Book.objects.filter(q_object)
    return render(request, 'searchResults.html', {'books': books, 'query': query})
