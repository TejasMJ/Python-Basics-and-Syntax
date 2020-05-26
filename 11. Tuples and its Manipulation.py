#Tuple - A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print('\n')

print('-------Accessing Elements of the Tuple-------')
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
print('\n')

print('-------Changing Elements of the Tuple-------')
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print('\n')

print('-------Deleting Elements of the Tuple-------')
'''
NOTE : Tuples are unchangeable, so you cannot remove items 
       from it, but you can delete the tuple completely
'''
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists
print('\n')

print('-------Joining Two Tuples-------')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


print('----------Other Importants------------')
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
