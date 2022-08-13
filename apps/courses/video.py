
from web.settings import BASE_DIR

def handle_uploaded_file(f):  
    with open(BASE_DIR+'/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  