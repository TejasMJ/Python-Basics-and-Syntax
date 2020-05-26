thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print('\n')

print('-------Accessing Elements--------')
print('----Version 1----')
x = thisdict["model"]
print(x)
print('----Version 2----')
x = thisdict.get("model")
print(x)
print('\n')

print('-------Changing Elements--------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
print('\n')

print('-------Looping through Dictionaries--------')
for x in thisdict:
  print(x)

print('\n')

for x in thisdict:
  print(thisdict[x])

print('\n')

for x in thisdict.values():
  print(x)
print('\n')

for x, y in thisdict.items():
  print(x, ':', y)

print(len(thisdict))
print('\n')

print('-------Adding Elements in the Dictionary--------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
print('\n')

print('-------Deleting Elements from the Dictionary--------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
print('\n')

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
print('\n')

print('-------Copying a Dictionary--------')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print('\n')

print('-------fromskey()--------')
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)
print('\n')

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)
print(thisdict)
print('\n')

print('-------Updating the value--------')
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(6):
  print(x)
else:
  print("Finally finished!")