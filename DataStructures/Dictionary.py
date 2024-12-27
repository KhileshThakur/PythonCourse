'''
Dictionary:
    - collection of key-value pairs 
    - mutable
'''

dict1 = {
    "name": "khilesh",
    "age": 22
}

print(dict1['name'])
print(dict1.get('age'))

dict1['age']=35
print(dict1)

dict1['gender']='Male'
print(dict1)

rem = dict1.pop('age')
print(dict1)

rem1=dict1.popitem()
print(rem1)

dict1.clear()
print(dict1)

dict2 = {
    "name": "khilesh",
    "age": 22,
    "city": "Bengluru"
}
print(dict2.keys())
print(dict2.values()) 
dict2.update({"name":"khilesh", "age":23, "city":"Pune"})
print(dict2)
for key in dict2:
    print(key)
for val in dict2.values():
    print(val)
for key, value in dict2.items():
    print(f"{key}:{value}")

nest_dict = {
    "person1":{
        "name": "khilesh",
        "age": 23
    },
    "person2": {
        "name": "vihaan",
        "age": 34
    },
    "person3": {
        "name": "avir",
        "age": 25
    }
}

print(nest_dict)
print(nest_dict["person1"])
print(nest_dict["person1"]["age"])

nest_dict['person4']={"name":"john", "age":33}
print(nest_dict)

#{1:1, 2:4, 3:9, 4:16, 5:25}
res = {x:x**2 for x in range(1, 6)}
print(res)

#retrive even nos
evn = {key:value for key, value in res.items() if key%2==0}
print(evn)

#
