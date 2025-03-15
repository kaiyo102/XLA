from django.shortcuts import render

# Create your views here.
def loginpage(request):
    message = """"""
    return render(request, 'Front/login.html', {'message': message})