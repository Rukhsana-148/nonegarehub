from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Data

# Create your views here.
def home(request):
    text = {'name':'Rukhsana Khatun', 'course': 'dJango'}
    return render(request, 'index.html',text)

#def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    values = val1+val2
    result = {'first' : val1, 'second' : val2,'sum':values}
    return render(request, 'result.html', result)

def dashboard(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def data (request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['pass']
        values = Data(email=email, name=name, password=password)
        values.save()
        return render(request, 'data.html')

   
   



