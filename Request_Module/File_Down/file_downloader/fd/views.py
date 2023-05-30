from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import os
import time

def download_by_url(url):
    try:
        name = url.split('/')[-1]
        if '?' in url:
            name = input('Enter Name For The File With Extension\n')
        
        if name in os.listdir('media'):
            return name
        
        else:

            r = requests.get(url, stream=True)
            with open(f"file_downloader/static/{name}", 'wb') as f:
                for i in r.iter_content(chunk_size=2000):
                    f.write(i)
                
            return name
        
    except Exception as e:
        print(e)
        print('Error Occured')
        return 'Enter The Correct Url'




def index(request):
    from fd.models import file
    filess = file.objects.all()
    return render(request, 'fd/index.html', {"files": filess, "f": filess[1::]}) 

@csrf_exempt
def success(request):
    from fd.models import file
    filess = file.objects.all()
    print(filess)
    Girl = request.POST.get('Girl', 'off')
    Zara = request.POST.get('Zara-Poly-Img', 'off')
    listed = []
    checked = []
    last = []
    files = []
    listed.append(f'{Girl} Girl')
    listed.append(f'{Zara} Zara')
    for i in listed:
        if not i.startswith('off'):
            checked.append(i)
    
    for char in checked[0]:
        if char not in [' ']:
            last.append(char)

    for i in filess:
        files.append(i)

    lasted = ''.join(last)

    url = ''

    if lasted == 'Girl':
        es = []
        for l in files:
            if str(l).endswith('(2)'):
                es.append(l)
        url = es[0].ob.url
    elif lasted == 'Zara':
        es = []
        for l in files:
            if str(l).endswith('(1)'):
                es.append(l)
        url = es[0].ob.url

    return render(request, 'fd/success.html', {"url": url})