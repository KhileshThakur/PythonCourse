'''
Json :
(javascript object notation)
'''

import json 

#Convert python object to json(json.dumps)

data = {
    "name": "khilesh", 
    "age": 34,
    "is_emp": True,
    "skills" : ["python", "c", "c++"]
}

result = json.dumps(data)
print(result)

#Convert json string to python object

json_str = '{"name": "khilesh", "age":34, "is_emp": true, "skills": ["python", "c", "c++"]}'
result = json.loads(json_str)
print(result)


data = {
    "name": "Khilesh",
    "age": 25,
    "is_emp": True
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
    
with open("data.json", 'r') as file:
    data=json.load(file)
    print(data)
    

#handling non serializable objectss
from datetime import datetime

data ={
    "name": "Khilesh",
    "timestamp": datetime.now()
}

# class Dteencoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         return super().default(obj)
# result = json.dumps(data, indent=4, cls=DateTimeEncoder) # type: ignore
# print(result)-------> WRONGGGGGGGGGGGGGGGGGGGGGGGGG


#parsing json arrays 
data = """
[
    {
        "name": "Khilesh", 
        "age" : 21
    },
    {
        "name": "Om",
        "age" : 21
    }
]
"""
result = json.loads(data)
for ele in result:
    print(f"{ele['name']}-{ele['age']}")
    
    
    
'''
Update the Json file 
{
    "name": "Khilesh",
    "age" : 22,
    "city" : "Pune"
}

update the age to 23 and save changes 
'''

with open("data.json", "r") as file:
    data=json.load(file)
data['age']=23
data['city']="Pune"
with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)


'''
json1={
    "name":"siri", "age":21
}
json2={
    "city":"pune", "job": "Developer"
}
program to merge these json object into one
'''

json1='{"name":"siri", "age":21}'
json2='{"city":"pune", "job": "Developer"}'
d1 = json.loads(json1)
d2 = json.loads(json2)
mergeData= {**d1, **d2}
print(json.dumps(mergeData))


