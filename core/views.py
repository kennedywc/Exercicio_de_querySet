from django.shortcuts import render
from .models import Book, Author, Tag, Review, Profile

from django.db.models.functions import Length
from django.db.models import Count


"""
def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='nome da tag')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='nome do autor')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()

    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
    }

    return render(request, 'core/teste1.html', context) 
"""


def query_examples(request):

    # EX a)
    autor_especifico = "Samuel Cavalcanti"
    livros_do_autor = Book.objects.filter(author__name=autor_especifico)

    # EX b)
    tag_especifica = "Ficção"
    livros_da_tag = Book.objects.filter(tags__name=tag_especifica)

    # EX c)
    palavra_ou_frase = "Quo facilis corporis."
    autores_com_biografia_especifica = Author.objects.filter(bio__icontains=palavra_ou_frase)

    # EX d)
    avaliacao_alta = Review.objects.filter(rating__gte=4).order_by('-rating')

    # Ex e)
    site = 'http://mendes.com/'
    usuario_website = Profile.objects.filter(website=site)

    # EX f)
    website_especifico = Book.objects.filter(reviews__isnull=True)

    # Ex g)
    autores_mais_livros = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')


    # Ex h)
    livros_resumos_longos = Book.objects.annotate(summary_length=Length('summary')).filter(summary_length__gt=150)

    # Ex i)
    nome_autor = "Samuel Cavalcanti"
    avaliacoes_do_autor = Review.objects.filter(book__author__name=nome_autor)

    # Ex j)
    tag_poesia = Tag.objects.get(name='Poesia')
    tag_ciencia = Tag.objects.get(name='Ciência')
    livros_tags_especificas = Book.objects.filter(tags__in=[tag_poesia, tag_ciencia])

    context = {
        'livros_por_autor': livros_do_autor,
        'livros_por_tag': livros_da_tag,
        'autores_com_biografia': autores_com_biografia_especifica,
        'avaliacao_alta': avaliacao_alta,
        'usuario_website': usuario_website,
        'website_especifico': website_especifico,
        'livros_resumos_longos': livros_resumos_longos,
        'avaliacoes_do_autor': avaliacoes_do_autor,
        'livros_tags_especificas': livros_tags_especificas,
        'autores_mais_livros': autores_mais_livros,
    }

    return render(request, 'core/teste1.html', context)