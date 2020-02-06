from django.shortcuts import render,redirect
from . models import User_register,Movies, Reviews

# Create your views here.

def index(request):

    movies = Movies.objects.all()

    return render(request,'index.html',{'movie':movies})


def movie_details(request,id):
    movie_detail = Movies.objects.filter(id=id)
    movie_reviews = Reviews.objects.filter(movie_id=id)
    sum = 0
    i =0
    for stars in movie_reviews:
        sum = sum + stars.rating
        i+=1
    if(i==0):
        sum = 0
    else:
        sum = sum/i
    
    return render(request,'loggedmd.html',{'movie_detail':movie_detail,'movie_reviews':movie_reviews,'rate':sum,'i':i})

def User_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pwd']

        new_user = User_register.objects.create(name=name,email=email,phone_no=phone,password=pwd)
        new_user.save()
        return redirect('/loginpage')
def loginpage(request):
    msg = 'Succesfully registered'
    return render(request,'login.html',{'msg':msg})
def login(request):
    if request.method == 'POST':
        email = request.POST['lemail']
        pwd = request.POST['lpwd']

        if User_register.objects.filter(email=email,password=pwd).exists():
            user = User_register.objects.filter(email=email,password=pwd)
            movies = Movies.objects.all()
            for x in user:
                request.session['username']=x.name
            
            return render(request,'loggedindex.html',{'movie':movies,'user':user})

def review(request):
    if request.method == 'GET':
        star = int(request.GET['star'])
        movie_id = request.GET['movie_id']
        title = request.GET['title']
        review = request.GET['review']
        username = request.session['username']

        Review = Reviews.objects.create(movie_id=movie_id,user_name=username,rating=star,title=title,review=review)
        Review.save()
        movie_detail = Movies.objects.filter(id=movie_id)
        movie_reviews = Reviews.objects.filter(movie_id=movie_id)
        sum = 0
        i =0
        for stars in movie_reviews:
            sum = sum + stars.rating
            i+=1
        if(i==0):
            sum = 0
        else:
            sum = sum/i
        return render(request,'loggedmd.html',{'movie_detail':movie_detail,'movie_reviews':movie_reviews,'rate':sum,'i':i})


def mregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pwd']

        new_user = User_register.objects.create(name=name,email=email,phone_no=phone,password=pwd)
        new_user.save()
        return redirect('/mloginpage')

def mloginpage(request):
    return render(request,'mlogin.html')

def mlogin(request):
    if request.method == 'POST':
        email = request.POST['lemail']
        pwd = request.POST['lpwd']

        if User_register.objects.filter(email=email,password=pwd).exists():
            movies = Movies.objects.all()

            return render(request,'loggedindex.html',{'movie':movies})

def quiz(request):
    return render(request, 'start.html')
def quizstart(request):
    return render(request, 'quiz.html')
def endquiz(request):
    return render(request,'end.html')

    

    

