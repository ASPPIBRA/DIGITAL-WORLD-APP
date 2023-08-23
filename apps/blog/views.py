from django.shortcuts import render
from apps.blog.models import BlogPost
from django.shortcuts import get_object_or_404


def blog_post(request):
    
    posts = BlogPost.objects.filter(main_post=False)
    main_posts = BlogPost.objects.filter(main_post=True)
    return render(request, 'home/blog.html', {'posts': posts, "main_posts": main_posts})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'home/blog_post_detail.html', {'post': post})