


'''
Give json File sales.json
{
    "sales":[
        {"region":"North", "amount":1000},
        {"region":"Sount", "amount":2000},
        {"region":"West", "amount":3000},
        {"region":"East", "amount":1000}
    ]
}
pragram to calculate the total sales in each region 
'''

'''
Given json file grades.json
{
    "grades::[
        {"name": "Alice", "score": 80},
        {"name": "Bob", "score": 80},
        {"name": "John", "score": 80},
    ]
}

- calculate the average score
- highest score
- minimum score

'''

'''
Write python program to validate
password based on the following criteria
- atleast 8 char long
- atleast 1 upper case
- atleast 1 lower case
- contains at least one special char (!@#$%^&())
'''


'''
Write a python program to find all 
palindromic words in a given sentence.
("Anna", "Bob", "Racecar")

'''


import re 
def pal_words(sentence):
    pattern = r"\b\w+\b"
    words=re.findall(pattern, sentence)
    palindromes=[word for word in words if word.lower() == word.lower()[::-1]]
    return palindromes
sentence= "madam tea to bob and anna"
pali_words=pal_words(sentence)
print(pali_words)


'''
Extract all text enclosed in double or single quotes from a paragraph 
ip: she said "Hello world" and added  'python is amazing ' language
'''

import re 
def extract_words(sentence):
    pattern=r'["\'][^"\']*["\']'
    quote_text=re.findall(pattern, sentence)
    return quote_text
sentence="she said \"Hello world\" and added  'python is amazing ' language"
result=extract_words(sentence)
print(result)


'''
valid time in 24 hour format 
task :
-   HH:MM format(24 hour clock)
-   ip: 23:45, 9:30 (valid),
        25:00, 12:60 (invalid)
'''



import re

def is_valid_time_24_hour_format(time_str):
    # Regular expression to match HH:MM format
    time_pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
    return bool(re.match(time_pattern, time_str))

# Test cases
test_times = ["23:45", "9:30", "25:00", "12:60", "00:00", "24:01", "19:59"]
for time in test_times:
    print(f"{time}: {'Valid' if is_valid_time_24_hour_format(time) else 'Invalid'}")
    
    
    
'''
Program to replace senstive information 
(EG: Credit card nos , phone nos, ) in string with
asteriks
'''

import re

def mask_sensitive_info(text):
    credit_card_pattern = r'\b(?:\d[ -]*?){13,16}\b'  # Matches 13-16 digit credit card numbers
    phone_number_pattern = r'\b\d{10}\b'  # Matches 10-digit phone numbers

    text = re.sub(credit_card_pattern, lambda x: '*' * len(x.group()), text)
    text = re.sub(phone_number_pattern, lambda x: '*' * len(x.group()), text)

    return text

input_text = """
My credit card number is 1234 5678 9012 3456, and my friend's card number is 9876-5432-1098-7654.
Call me at 9876543210 or on my office number 1234567890. My backup card is 123456781234.
"""

output_text = mask_sensitive_info(input_text)

print("Original Text:\n", input_text)
print("\nMasked Text:\n", output_text)


'''
Program to split camelcase string into individual words
input: CamelCaseExample ---> Camel Case Example
'''

def split_camel_case(input_string):
    split_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return split_string

input_text = "CamelCaseExample"
output_text = split_camel_case(input_text)

print("Input:", input_text)
print("Output:", output_text)