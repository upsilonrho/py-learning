import json

myPets = ["cat", "dog", "rabbit"]
myData = [1, 3, 6, 8, 7, 4]
x = [myPets, myData]
y = 5, 6, 7, 1
z = x, y
print(z)
print(z[0])
print(z[1])
print(z[0][0][2])
print(z[1][2])

myStr = json.dumps(z)
print(myStr)

with open('testjson.txt', 'w') as fout:
    json.dump(z, fout)

with open('testjson.txt', 'r') as fin:
    read_data = json.load(fin)

print(read_data)
print(read_data[0])
print(read_data[1])
print(read_data[0][0][2])
print(read_data[1][2])
