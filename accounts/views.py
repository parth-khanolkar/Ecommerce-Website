from django.shortcuts import render

# Create your views here.
def LoginPage(request):
    return render(request, 'login.html')

def LogoutPage(request):
    return render(request, 'logout.html')