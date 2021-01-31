from django.shortcuts import render

# error pages

def bad_request(request, exception):
    return render(request,'errors/page_400.html')

def permission_denied(request, exception):
    return render(request,'errors/page_403.html')
 
def page_not_found(request, exception):
    return render(request,'errors/page_404.html')

def server_error(request):
    return render(request,'errors/page_500.html')
