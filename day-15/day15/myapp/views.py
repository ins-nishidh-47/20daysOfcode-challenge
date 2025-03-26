from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.all()  # Fetch all blogs from the database
    return render(request, "home.html", {"blogs": blogs})
