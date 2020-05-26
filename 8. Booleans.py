print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))

print('-----------Function Part----------')
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

def myFunction1() :
  return True

print(myFunction1())

print('------------isintance--------------')
x = 200
print(isinstance(x, int))