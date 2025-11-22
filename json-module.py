import json

# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
# y = json.loads(x)
#
# print(y)

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x, indent=4, sort_keys=True)

# the result is a JSON string:
print(y)