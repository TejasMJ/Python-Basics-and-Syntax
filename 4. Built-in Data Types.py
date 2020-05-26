'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''

#----------------Getting the Data-type--------------
x = 5
print(type(x))

x = memoryview(bytes(5))
print(x)

#---------------Something new with Memory View---------

a = b'Hey !'
print(type(a))
print(memoryview(a))
b = memoryview(a)
print(b.obj)
