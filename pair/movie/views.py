from django.shortcuts import redirect, render
from .models import Review

# Create your views here.


def index(request):
    _movie = Review.objects.all()

    context = {
        "movie": _movie,
    }
    return render(request, "movie/index.html", context)


def create(request):
    content = request.GET.get("content_")
    title = request.GET.get("title_")
    textarea = request.GET.get("textarea_")

    Review.object.create(title=title, content=textarea)

    return redirect("movie:index")

def review(request):
    return render(request, "movie/review.html")
