from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def about_site(request):
    return render(request, 'core/about_site.html')


def books(request):
    return render(request, 'core/books.html')

def book_taina(request):
    return render(request, 'core/book_taina.html')

def book_devyatyi_dom(request):
    return render(request, 'core/book_devyatyi_dom.html')

def book_zlodei(request):
    return render(request, 'core/book_zlodei.html')

def book_shesterka(request):
    return render(request, 'core/book_shesterka.html')


def authors(request):
    return render(request, 'core/authors.html')

def author_donna(request):
    return render(request, 'core/author_donna.html')

def author_rio(request):
    return render(request, 'core/author_rio.html')

def author_bardugo(request):
    return render(request, 'core/author_bardugo.html')

def author_blake(request):
    return render(request, 'core/author_blake.html')


def news(request):
    return render(request, 'core/news.html')

def article_reading(request):
    return render(request, 'core/article_reading.html')

def article_adaptations(request):
    return render(request, 'core/article_adaptations.html')

def article_playlist(request):
    return render(request, 'core/article_playlist.html')
