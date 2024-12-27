'''
Write a class library that manages books
add a book
display all books 
return a book
'''

class library:
    def __init__(self):
        self.books=[]
        
    def addBook(self, name, author):
        book = {"name": name, "author": author}
        self.books.append(book)
        
    def printBooks(self):
        return self.books 
    
    def returnBook(self, name):
        for book in self.books:
            if book["name"].lower() == name.lower():
                self.books.remove(book)
                print(f'Book "{name}" returned to the library.')
                return
        
    
lib = library()
lib.addBook("ABC", "abc")
print(lib.printBooks())
lib.addBook("XYZ", "abc")
print(lib.printBooks())
lib.addBook("JCB", "abc")
print(lib.printBooks())
lib.returnBook("ABC")
print(lib.printBooks())


'''
Create a base class Employee with attribute name , id , salary
create subclass
1. manager : add dept attribute
2. developer : add a programming lang attribute
'''

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id=emp_id
        self.salary=salary
    def display_info(self):
        return f"Id: {self.emp_id}, name: {self.name}, salary: {self.salary}"
    
class manager(Employee):
    def __init__(self, name, emp_id, salary, dept):
        super().__init__(name, emp_id, salary)
        self.dept=dept
    def display_manager_info(self):
        return super().display_info()+f" Dept: {self.dept}"
    
man1 = manager("Alice", 1, 20000, "IT")
print(man1.display_manager_info())

'''
Create a class student that stores a students name , rollno, marks 
in three subjects 
- calculate the total and average marks
- determine the grade(A, B, C) based on the average
- display all the students details


'''

# class Student:
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks