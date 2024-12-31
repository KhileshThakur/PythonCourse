'''
Regular Expression : Powerful way to work with 
text by searching matching and manipulating patterns

'''

import re

#re.match()
result = re.match(r"Hello", "Hello World")
print(result)

#re.search()
res = re.search(r"world", "Hello world")
print(res)

#re.findall()
resnew = re.findall(r"\d+", "There are 12 cats and 10 dogs")
print(resnew)

#re.sub()
resn = re.sub(r"\d", '#', "There are 12 cats and 10 dogs")
print(resn)

#re.split()
# resnn = re.split(r'\s+' 'split the words in this stmt')
# print(resnn)


'''
. : any char except a newline
^ : matches the start of a str
$ : matches at the end of string
* : matches 0 or more representation
+ : matches 1 or more representaiton
? : matches 0 or 1 occurance
[] : matches any char within brackets
| : represent or
\ : Escapes special chars
'''

#extracting email address
# sales@comp.com

text = "contact me with support@test.com or sales@comp.com"
email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print(email)


#validating the phone no 
phone="123-456-7890"
pattern = r'^\d{3}-\d{3}-\d{4}$'
if re.match(pattern, phone):
    print("valid phone no.")
else:
    print("invalid phone no")
    
#replace multiple spaces with single space

text = "This            is           a    sentence"
result = re.sub(r'\s+', ' ', text)
print(result)


#Extracting words starting with a specific letter

Text = "python is practical oriented lang and popular too"
words = re.findall(r'\bp\w*', Text)
print(words)

#find all hashtags from the msg
msg = 'python program #language loves # everyone#'
result = re.findall(r'#+', msg)
print(result)

#find repeated words
text = "This is a text of text only"
res=re.findall(r'\b(\w+)\b(?=.*\b\1\b)', text)
print(res)


#checking for strong password
password = "Password@3244"

#extract words start with vowels (a, e, i, o, u)
Text = "Apple is not the only thing that keep everybody away from doctor"
words = re.findall(r'\b[aeiouAEIOU]\w*', Text)
print(words)


#validating the filenames 
'''(.txt, .csv, .json)'''
files = ["file.txt", "data.csv", "img.jpg", "data.json", "pic.png"]
pattern = r'.*\.(txt|csv|json)$'

for i in files:
    if re.match(pattern, i):
        print(f"{i} is valid ")
    else:
        print(f"{i} is invalid")


#identifying the repeated char
text = "I iceeee creeeem idddddsss"
repeated_chars = re.findall(r'(.)\1+', text)
print(repeated_chars)
pattern = r"(\w)\1{2,}"
res = [match.group(0) for match in re.finditer(pattern , text)]
print(res)


