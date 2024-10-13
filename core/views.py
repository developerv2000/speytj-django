from django.shortcuts import render

def home(request):
    return render(request, 'core/pages/home.html', {'my_list': [1,2,3,4]})
