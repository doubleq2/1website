from django.shortcuts import render
#
def index(request):
    return render(request, 'web_site/index.html')


def about(request):
    return render(request, 'web_site/about.html')   


def geography(request):
    return render(request, 'web_site/geography.html')   


def papers(request):
    return render(request, 'web_site/papers.html')   


def photo(request):
    return render(request, 'web_site/photo.html')   


def thanks(request):
    return render(request, 'web_site/thanks.html')   


def people(request):
    return render(request, 'web_site/people.html')   