from django.shortcuts import *
from django.http import *
from books.models import books
from books.forms import *
from django.db import models
def index(request):
    return HttpResponse("Hello, world. You're at the books index.")
# Creating a web page to view all and with a search functionality
def search(request):
    authorform = authorForm()
    titlesearchform2 = titlesearchform()
    descriptionsearchform2 = descriptionsearchform()
    if request.method == 'POST':
    	if "Title" in request.POST:
    		titlesearchform2 = titlesearchform(request.POST)
    		if titlesearchform2.is_valid():
    			Title = titlesearchform2.cleaned_data['Title']
    			if Title:
    				return render(request, 'books/filter.html',{'form': authorform, 'form2':titlesearchform2, 'form3':descriptionsearchform2, 'obj1': books.objects.filter(Title__icontains=Title)})
    	elif "Description" in request.POST:
    		descriptionsearchform2 = descriptionsearchform(request.POST)
    		if descriptionsearchform2.is_valid():
    			Description = descriptionsearchform2.cleaned_data['Description']
    			if Description:
    				return render(request, 'books/filter.html',{'form': authorform,'form2':titlesearchform, 'form3':descriptionsearchform2, 'obj1': books.objects.filter(Description__icontains=Description) })
    	elif "Author" in request.POST:
    		authorform = authorForm(request.POST)
	    	if authorform.is_valid():
	    		Author = authorform.cleaned_data['Author']
	    		if Author and Author != 'none':
	    			return render(request, 'books/filter.html',{'form': authorform,'form2':titlesearchform2, 'form3':descriptionsearchform2,'obj1': books.objects.filter(Author=Author)})
	    	else:
	    		render(request, 'books/filter.html',{'form': authorform,'form2':titlesearchform2, 'form3':descriptionsearchform2,'obj1': books.objects.all()})
    return render(request, 'books/filter.html',{'form': authorform, 'form2':titlesearchform2, 'form3':descriptionsearchform2,'obj1': books.objects.all()})

#Creating a function to add entries into the books database
def addbook(request): 
	if request.method == 'POST':
		form = booksForm(request.POST)
		if form.is_valid():
			u = form.save()
			return redirect('/books/search')
	else:
		form = booksForm()
	return render(request, 'books/details.html', {'form': form,})