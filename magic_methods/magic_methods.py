class Book:
    def __init__(self,title,author,pages) :
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self) :
        '''This method defines the string representation of an object. 
        It's called when you use the `str()` function or the `print()` 
        function on an instance of the class.   '''
        return f'{self.title} by {self.author}'
    
    def __repr__(self) :
        return f"Book({self.title}, {self.author}, {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __add__(self,other_book):
        total_pages = self.pages + other_book.pages
        return Book('Combined Book',f'{self.author} & {other_book.author}',total_pages)
    
    def __eq__(self, other_book):
        return self.pages == other_book.pages
    
    def __lt__(self,other_book): #__le___ <=
        return self.pages < other_book.pages
    
    def __gt__(self,other_book): # __ge__ >=
        return self.pages > other_book.pages
    
    def __getitem__(self,key):
        if key == 'author':
            return self.author
        
        elif key == 'title':
            return self.title
        
        elif key == 'pages':
            return self.pages
        
        else :
            return 'invalid keyword'
        
    def __setitem__(self,key,value) :
        if key =='title':
            self.title = value
        elif key == 'author':
            self.author = value
        elif key =='pages':
            self.pages = value
        else :
            return 'invalid keyword'
    
    def __call__(self,publisher) :
        return f'{self.title} is ready for publishing by {publisher}'   
    
book1=Book("To Kill a Mockingbird", "Harper Lee", 320)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(book1)
print(repr(book1))
print('number of pages : ', len(book1))
combined_book = book1 + book2
print(combined_book)
print('number of pages : ',len(combined_book))
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
title = book1['title']#book1.title
print(title)
author = book2['author']
print(author)
book2['author']='some author that i forgot his name'
print(book2['author'])
print(book1('some publisher'))
print(callable(book1))