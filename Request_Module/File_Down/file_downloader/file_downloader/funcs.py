import requests
import os

def download_by_url(url):
    try:
        name = url.split('/')[-1]
        if '?' in url:
            name = input('Enter Name For The File With Extension\n')

        r = requests.get(url, stream=True)
        # os.chdir('')
        with open(f"file_downloader/static/{name}", 'wb') as f:
            for i in r.iter_content(chunk_size=128):
                f.write(i)
            
        return name
    except Exception as e:
        print(e)
        print('Error Occured')
        return 'Enter The Correct Url'

