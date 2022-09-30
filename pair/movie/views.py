from django.shortcuts import redirect, render
from .models import Review

# Create your views here.

def index(request):
    _movie = Review.objects.all()

    context = {
        "movies": _movie,
    }

    return render(request, "movie/index.html", context)

def create(request):
    title = request.GET.get("title_")
    textarea = request.GET.get("textarea_")

    Review.objects.create(title=title, content=textarea)

    return redirect("movie:index")

def review(request):
    return render(request, "movie/review.html")

def detail(request, movie_pk):
    pk_ = Review.objects.get(pk = movie_pk)

    context = {
        "pk": pk_
    }

    return render(request, "movie/detail.html", context)

def edit(request, edit_pk):
    content = request.GET.get("u_title")
    content2 = request.GET.get("u_textarea")

    pk = Review.objects.get(pk = edit_pk)
    pk.title = content
    pk.content = content2
    pk.save()

    return redirect("movie:index")

def delete(request, delete_pk):
    movie = Review.objects.get(pk = delete_pk)
    movie.delete()

    return redirect("movie:index")

# 리뷰 수정 버튼 -> 수정 페이지
def update(request, update_pk):
    update_ = Review.objects.get(pk = update_pk)
    
    context = {
        'update': update_
    }

    return render(request, "movie/edit.html", context)