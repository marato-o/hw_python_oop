from django.shortcuts import HttpResponse, render
from .models import Post

def index(request):
    latest = Post.objects.order_by('-pub_date')[:10]
    """
    output = []
    for item in latest:
        output.append(item.text)
    return HttpResponse('\n'.join(output))
    """
    return render(request, "index.html", {"posts":latest})
    

# Create your views here.
