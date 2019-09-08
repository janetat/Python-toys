import requests
from celery_app import app

@app.task
def add(a, b):
    print('add a and b: ', a+b)
    return a + b


@app.task
def download_img(url):
    print(url)
    response = requests.get(url)
    with open('img.jpg', 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
