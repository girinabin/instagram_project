from django.shortcuts import render
from .models import post
from .forms import CreateArticle
# Create your views here.
def add_blog(request):
    form = CreateArticle()
    if request.method == 'POST':
        form = CreateArticle(request.POST,request.FILES)#request.FILES must important
        if form.is_valid():
            form.save()
    return render(request,'posts/add_post.html',{'form': form})

def home(request):
    poost = post.objects
    return render(request,'posts/home.html',{'post1':poost})