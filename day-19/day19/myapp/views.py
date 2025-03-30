from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# Add a dummy view to test 404 (Optional)
def home(request):
    return render(request, 'home.html')
