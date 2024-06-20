import json
'''a=open("file1.json","r")
b=json.load(a)
print(b)
print(type(b))
file1.close()'''
file=open("file.json", "w")

data={
    "name":"Abhinaya",
    "roll":"23951a0504",
    "mobile":9992929239

}

json.dump(data,file)
file.close()