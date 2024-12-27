# file_obj = open("filename", 'mode')
'''
r: read mode
w: write mode
a: append mode
b: binary mode
x: exclusive creation(creates the new file, but fails if the file already exist)
'''

#Reading file:
'''
read(): read entire file
readline(): reads one line at a time
readlines(): reads all the lines into a list
'''

with open("file.txt", 'r') as file:
    content=file.read()
    print(content)

#reading line by line

with open('file.txt', 'r') as file:
    for line in file:
        print(line, end="")
    
with open('file.txt', 'r') as file:
    lines=file.readlines()
    print(lines)


#writting to file 
'''
write(): writes a string to the file 
writelines(): writes the 
'''

with open('file.txt', 'w') as file:
    file.write("Hello World")
    file.write("This is Python!")
    
lines = ['Hi, \n', 'My name is Khilesh Thakur\n', 'I am Computer Engineering \n', 'I like coding and I am interested in website development\n']
with open("file.txt", 'w') as file:
    file.writelines(lines)

with open('file.txt', 'a') as file:
    file.write("Lets append a line by programming")


f1=open("file.txt", 'r')
content=f1.read()
print(content)
f1.close()

try:
    with open("abc.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File Not FOUND!")
except IOError:
    print("Error in reading file !")
    
'''
seek(): moves the file pointer to specific location and 
tell(): returns the current position of file position 

'''

with open("file.txt", 'r') as file:
    file.seek(10)
    print(file.tell())
    content = file.read()
    print(content)
