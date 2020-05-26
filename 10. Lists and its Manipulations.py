'''

There are four collection data types in the Python programming language:

List  - is a collection which is ordered and changeable.
        Allows duplicate members.
Tuple - is a collection which is ordered and unchangeable.
        Allows duplicate members.
Set   - is a collection which is unordered and unindexed.
        No duplicate members.
Dictionary - is a collection which is unordered, changeable
             and indexed. No duplicate members
'''

ListofFruits = ['Apple','Cherry','Banana']
print(ListofFruits)

print('------------------Silicing of the List.----------------')
ListofFruits = ['Apple','Cherry','Banana']
print(ListofFruits[1])

print(ListofFruits[-1])

print(ListofFruits[:2])
print('\n')

print('------------------Changing the Values.----------------')
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print('\n')

print('------------------Adding Items.----------------')
print('-----Version 1-----')
print('Before Adding')
ListofFruits = ['Apple','Cherry','Banana']
print(ListofFruits)
print('After Adding')
ListofFruits.append('Orange')
print(ListofFruits)

print('-----Version 2-----')
thislist = ["apple", "banana", "cherry"]
print('Before Adding')
print(thislist)
thislist.insert(1, "orange")
print('After Adding')
print(thislist)
print('\n')

print('------------------Removing Items.----------------')
thislist = ["apple", "banana", "cherry"]
thislist.remove('banana')
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() #The pop() method removes the specified index, (or the last item if index is not specified):
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print('\n')

print('------------------Clearing the List.----------------')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print('\n')

print('------------------Copying List.----------------')
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print('\n')

print('------------------Joining Lists.----------------')
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
print('\n')

print('----------------------------------------------------')
List1 = ['Banana','Apple','Jackfruit','Dragon-Fruit']
List1.reverse()
print(List1)

List1.sort()
print(List1)
