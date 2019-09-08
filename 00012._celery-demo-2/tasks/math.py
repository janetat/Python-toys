from celery_app import app

@app.task
def add(a, b):
    print('add a and b: ', a+b)
    return a + b