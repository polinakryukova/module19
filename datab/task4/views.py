from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    items_per_page = int(request.GET.get('items_per_page', 3))
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fourth_task/index.html', {'page_obj': page_obj})