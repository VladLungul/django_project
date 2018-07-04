

from django.shortcuts import render
from .models import Post

from string import punctuation

def clear_text(text):
    table = str.maketrans('', '', punctuation)
    return text.translate(table)

def unique_words(qs):
    post = qs.text
    cleared = clear_text(post)
    return len(set(cleared.split()))

def sort_posts(posts):
    return sorted(posts, key=unique_words, reverse=True)


def index(request):
    if request.method == "POST":
        text = request.POST.get('text_post')
        post = Post(text=text)
        post.publish()
    posts = Post.objects.all()
    posts = sort_posts(posts)
    return render(request, 'blog/post_list.html', {'posts': posts} )