from django.http import HttpResponse
from django.template import loader
from .models import query

def index(request):
    template = loader.get_template('farewell/index.html')
    context = {}
    return(HttpResponse(template.render(context, request)))

    
def contact(request):
    # /contact
    template = loader.get_template('farewell/contact.html')
    context = {}
    return(HttpResponse(template.render(context, request)))
    

def addquestion(request):
    q = query(name=request.POST['uname'], email=request.POST['uemail'], text=request.POST['text'])
    q.save()
    return(HttpResponse('Added.</a>'))
    
    
def showquestions(request):
    page = ""
    for q in query.objects.all():
        page = page+q.name+'<br>'+q.email+'<br>'+q.text+'<br><br>'
    return(HttpResponse(page))