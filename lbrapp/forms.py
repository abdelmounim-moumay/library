from django import forms 
from.models import Book, Category
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title',
                  'author',
                  'photo_book',
                  'photo_author',
                  'pages',
                  'price',
                  'status',
                  'Category',
                  ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'Category': forms.Select(attrs={'class':'form-control'}),
        }