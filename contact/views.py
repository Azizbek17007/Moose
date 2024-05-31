from django.shortcuts import render

from blog.models import Author, About


# Create your views here.
def about_page(request):
    author = Author.objects.all().order_by('id')[:1]
    abouts = About.objects.all().order_by('id').first()
    context = {'author': author, 'abouts': abouts}
    return render(request, 'about.html', context)