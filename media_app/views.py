from django.shortcuts import render, redirect
from media_app.models import Post, LikePost
from django.contrib.auth.decorators import login_required

def get_data(request, key):
    return request.GET.get(key) or request.POST.get(key)

# Create your views here.
def index_view(request):
    page_name = "index.html"
    data = {
        "posts" : Post.objects.all().order_by('-created_at')
    }
    return render(request, page_name, context=data)

@login_required(login_url='sign_in')
def submit_post(request):
    user = request.user
    content = get_data(request, 'post_caption')
    image = request.FILES.get('post_image')
    Post.objects.create(
        user=user,
        caption=content,
        image=image
    )
    return redirect('index')

@login_required(login_url='sign_in')
def like_post(request):
    user = request.user
    post_id = get_data(request, 'post_id')
    LikePost.objects.create(
        user_id=user.id,
        post_id=post_id
    )
    # or 
    # post = Post.objects.get(id=post_id)
    # LikePost.objects.create(user=user, post=post)
    return redirect('index')