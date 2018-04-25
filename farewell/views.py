from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('farewell/index.html')
    context = {}
    return(HttpResponse(template.render(context, request)))

    
def contact(request):
    # /contact
    return(HttpResponse(''))