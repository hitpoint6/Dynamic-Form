from django.shortcuts import render, redirect
from django.views.generic.list import ListView


from .forms import BookFormset
from .models import Book

def create_book_normal(request):
    template_name = 'create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


class BookListView(ListView):
    model = Book
    template_name ='book_list.html'