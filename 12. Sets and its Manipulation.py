#Set - A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

print('-------Accessing Elements of the Set.-------')
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print('\n')

print('-------Adding Elements of the Set.-------')
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)
print('\n')

print('-------Deleting Elements from a Set.-------')
print('----Version 1----')
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

print('----Version 2----')
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

print('----Version 3----')
#Remove the last item by using the pop() method
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
print('\n')

print('-------Clearing Elements from a Set.-------')
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
print('\n')

print('-------Joining two sets.-------')
print('----Version 1----')
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print('----Version 2----')
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
print('\n')

print('-------Copying sets.-------')
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
print('\n')

print('-------Difference between sets.-------')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
print('\n')

print('-------difference_update between sets.-------')
#Remove the items that exist in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
print('\n')

print('-----------Set Operations-----------------')
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)