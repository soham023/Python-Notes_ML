info = [
    ("Soham", "Math"),
    ("Sam", "History"),
    ("Mel", "Zoology"),
    ("Tenz", "Math"),
    ("Charlie", "English")
]
newset = set()
for inf in info:
    newset.add(inf[1])

print(newset)

engStudent = []
for inf in info:
    if(inf[1] == "English"):
        engStudent.append(inf[0])

print(engStudent)

divDict = {}
for i in info:
    if(divDict.get(i[0]) == None):
        divDict.update({i[0]: set()})
        divDict[i[0]].add(i[1])
    else:
        divDict[i[0]].add(i[1])

print(divDict)


