from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
#tecka znamena, ze je to ve stejnem adresari

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #kuri zavorky jsou to, co predavame sablne a pojmeonavni

def post_detail(request, pk):
     post = get_object_or_404(Post, pk=pk)
     return render(request, 'blog/post_detail.html', {'post': post})
