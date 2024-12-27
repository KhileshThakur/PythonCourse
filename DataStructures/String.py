rep="fa"*3
print(rep)

# Accessing and slicing

s = "Python is my world"
print(s[0])
print(s[-1])
print(s[1:7])
print(s[:3])
print(s[5:])

#Text transformation

text = "Hello Python, You look so good. AND YOU ARE AWESOME !!"
print(text.upper())
print(text.lower())
print(text.capitalize())


#Finding and replacing

print(text.find("Python"))
print(text.replace('Python', 'Javascript'))

str="   Hello   Python, You are so good.   "
print(str.strip())

#Checking Condition
print(text.startswith('Hello'))
print(text.endswith('!'))


#string formatting

name="siri"
age=30
print(f"my name is {name}, and i am {age} years old!")
print("my name is {} and i am {} years old".format(name, age))
print("my name is %s and i am %d years old"%(name, age))

#escape sequence

print("line1 \n line2")
print("line1\tline2")
print("backslash\\")


#Immutable 
str="Hello Python!"
#str[0]='F' #Its immutable......!


# Reversing string

str = 'python'
res=str[::-1]
print(res)

#Extract all vowels from string

str1="this is a python class"
vow=" ".join([char for char in str1 if char.lower() in 'aeiou'])
print(vow)

#Alternate letter capital
alterStr="This is alternate text to work on"
res="".join([char.upper() if i%2==0 else char.lower() for i, char in enumerate(alterStr)])
print(res)

#Remove digits from string
s="WonderFul11 theory34 o6f nat90ural languag9e"
res="".join([char for char in s if not char.isdigit()])
print(res)

#Find palindrome substrings

s="abcbcddcdabnbadnnp"


#compress a string by replacing consicutive chars with counts

s = "aaabbcddddddee"
