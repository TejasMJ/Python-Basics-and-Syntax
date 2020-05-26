
#---------------Let's play with Global Variables--------

x = 'Python is Awesome !'

def myfunction():
    print(x)

myfunction()

#-------------------------------------------------------
#--------------------Global Keyword--------------------

#-----Version 1-------------
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#-----Version 2-------------
def myfunc():
  global x
  x = "fantastic"

print("Python is " + x)

#-----Version 3 : Tricky but solvable---------
x = "awesome"

def myfuncv2():
  global x
  x = "fantastic"

myfuncv2()

print("Python is " + x)