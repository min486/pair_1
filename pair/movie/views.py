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

def edit(request):

    return redirect("movie:edit.html")

