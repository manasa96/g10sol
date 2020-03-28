# import form class from django 
from django import forms 
  
from .models import books 
  
# Creating a model form to add entries of books
class booksForm(forms.ModelForm): 
    class Meta: 
        model = books 
        fields = "__all__"
        widgets = {
        	'Author': forms.TextInput(attrs={'class' : 'myclass', 'placeholder':'Enter the author\'s name ..'}),
            'Title': forms.TextInput(attrs={'class': 'myclass','placeholder':'Enter the title of the book ..'}),
            'Description': forms.Textarea(attrs={'class': 'myclass2','placeholder':'Enter description of the book ..'}),
        }

def choicelist():
	Choice = books.objects.order_by('Author').values_list('Author', flat=True).distinct()
	d = [('none', 'None')]
	for x in Choice:
		d.append((x,x))
	return d
#Creating Form for search functionality
class titlesearchform(forms.Form):
	Title = forms.CharField(max_length=100, required= False, widget=forms.TextInput({'class' : 'myclass','placeholder':'Search for Titles ..','name':'title'}))
	def clean(self):
		cleaned_data = super(titlesearchform, self).clean()
		return cleaned_data   

class descriptionsearchform(forms.Form):
	Description = forms.CharField(max_length=1000, required= False, widget=forms.TextInput(attrs={'class' : 'myclass','placeholder':'Search for Description ..','name':'desc'}))
	def clean(self):
		cleaned_data = super(descriptionsearchform, self).clean()
		return cleaned_data 
		
class authorForm(forms.Form):
	#Choices to select the name of the author
	d=choicelist()
	#Title = forms.CharField(max_length=100, required= False, widget=forms.TextInput({'class' : 'myclass','placeholder':'Search for Titles ..'}))
	#Description = forms.CharField(max_length=1000, required= False, widget=forms.TextInput(attrs={'class' : 'myclass','placeholder':'Search for Description ..'}))
	Author = forms.CharField(widget=forms.Select(attrs={"onChange":'form.submit()','class':'myclass2' },choices=d), required= False)
	def clean(self):
		cleaned_data = super(authorForm, self).clean()
		field1 = cleaned_data.get("Title")
		field2 = cleaned_data.get("Description")
		field3 = cleaned_data.get("Author")
		fields = [field1, field2, field3]
		fields_selected = [field for field in fields if field]
		if len(fields_selected)>2 and field3 == 'none' : 
			raise forms.ValidationError('Please search from only one value')
		if len(fields_selected)>1 and field3 != 'none' : 
			raise forms.ValidationError('Please select only one value')
		return cleaned_data     
	def __init__(self, *args, **kwargs):
		super(authorForm, self).__init__(*args, **kwargs)
		self.fields['Author'] = forms.CharField(widget=forms.Select(attrs={"onChange":'form.submit()','class':'myclass2' },choices=choicelist()), required= False)
