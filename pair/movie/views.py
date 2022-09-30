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

    Review.object.create(content=content)

    return redirect("movie:index")

def review(request):
    return render(request, "movie/review.html")
