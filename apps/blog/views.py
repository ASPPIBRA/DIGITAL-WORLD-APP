from django.shortcuts import render
from django.http import JsonResponse
from apps.blog.models import BlogPost
from django.shortcuts import get_object_or_404

def blog_post(request):
    prefix = "https://"
    suffix = ".ipfs.w3s.link/"
    
    posts = BlogPost.objects.filter(main_post=False)
    main_posts = BlogPost.objects.filter(main_post=True)
    
    # Criar uma lista de dicionários para os posts principais
    main_posts_with_urls = []
    for post in main_posts:
        full_url = f"{prefix}{post.cid}{suffix}{post.file_name}"
        main_posts_with_urls.append({
            'post': post,
            'full_url': full_url
        })
        
    # Criar uma lista de dicionários para os posts não principais
    posts_with_urls = []
    for post in posts:
        full_url = f"{prefix}{post.cid}{suffix}{post.file_name}"
        posts_with_urls.append({
            'post': post,
            'full_url': full_url
        })
    
    return render(request, 'home/blog.html', {'posts_with_urls': posts_with_urls, 'main_posts_with_urls': main_posts_with_urls})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    prefix = "https://"
    suffix = ".ipfs.w3s.link/"

    try:
        image_object = BlogPost.objects.get(pk=post_id)
    except BlogPost.DoesNotExist:
        return JsonResponse({'status': 'failed', 'message': 'Image not found'})

    full_url = f"{prefix}{image_object.cid}{suffix}{image_object.file_name}"

    return render(request, 'home/blog_post_detail.html', {'post': post, 'full_url': full_url})
