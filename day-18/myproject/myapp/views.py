from django.shortcuts import render

def template_demo(request):
    data = {
        "name": "Nishidh",
        "age": 18,
        "marks": 75,
        "students": ["Alice", "Bob", "Charlie"],
    }
    return render(request, "myapp/demo.html", data)
