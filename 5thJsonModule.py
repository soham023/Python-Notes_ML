import json
# s in loads/dumbs stands for string
# when we convert json string to python obj
# json.loads()
json_str = '{"name" :"soham", "isTwacher": false}'
py_obj = json.loads(json_str)
print(py_obj)

# json.dumps()
# dumps does the opposite to loads
# converts pyobj to jsonstr



# when we deal with files then we use these 2 functions
# json.load()
# json.dump()