from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .funcs import download_by_url


def index(request):
    return render(request, 'index.html') 

@csrf_exempt
def success(request):
    user_url = request.POST.get('url')
    name = download_by_url(user_url)
    print(user_url, name)
    if name == 'Enter The Correct Url':
        return render(request, 'error.html')
    else:
        return render(request, 'success.html', {"name": name})