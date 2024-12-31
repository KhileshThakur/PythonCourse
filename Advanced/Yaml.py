'''
Yaml : yet another markup language
-   human readable data format used for 
    configuration file
-   comments are allowed
'''

import yaml  # type: ignore


#Yaml to Python 

yaml_string = """
name: Khilesh
age: 21
skills:
    - python
    - c
    - c++
    - java
"""

data=yaml.safe_load(yaml_string)
print(data)


#Python obj to Yaml 
data = {
    "name": "Khilesh", 
    "age" : 22,
    "Hobby": ["Reading", "Travelling"]
}
result = yaml.dump(data, default_flow_style=False)
print(result)


with open("yy.yaml", "w") as file:
    yaml.dump(data, file)


with open("yy.yaml", "r") as file:
    data=yaml.safe_load(file)
print(data)


