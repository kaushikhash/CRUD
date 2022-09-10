from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm,UserRegistrationForm

from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,f'Your account has been successfully created.You can login now')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        
    context = {'form':form}
    return render(request,'register.html',context)




def index(request):
    return render(request,'index.html')

def show(request):
    review = Review.objects.all()
    return render(request,'show.html',{'reviews':review})


    
def create(request):
    if request.method == "POST":
        new_review = Review (
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            description = request.POST.get('description'),
            review = request.POST.get('review')
        )
        new_review.save()
        return redirect('index')
    return render(request,'create.html')


def delete(request,pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('show')


def edit(request,pk):
    review = Review.objects.get(id=pk)
    return render(request,'edit.html',{'reviews':review})
    
def update(request,pk):
    
    reviews = Review.objects.get(id=pk)
    form = ReviewForm(request.POST,instance=reviews)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request,'edit.html',{"reviews":reviews})