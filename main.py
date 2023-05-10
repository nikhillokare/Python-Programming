# this is comment
print("Hello World")

# Variable
x = 5
y = "Hello World"
print(x,y)

#Indentation
if (5>2):
  print("Five is greater than two")
else:
  print("Five is lesser than two")

Casting
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

get Type
x = 5
y = "Nikhil"
z = True
a = 3.9
print(type(x))
print(type(y))
print(type(z))
print(type(a))

Double Quotes and single
x = 'Nikhil'
y = "Aniket"
print(x,y)

Case Sensitive
a = 4
A = "Nikhil"
print(a,A)

variables(legal)
var = "Nikhil"
v_ar = "Nikhil"
VAR = "Nikhil"
_Var = "Nikhil"
VAR2 = "Nikhil"
print(VAR)

illegal
2var = 3
v ar = 4
v-ar = 6

Python variable Assign multiple value
Many variables to many values
x,y,z = 2,3,4
print(x,y,z)

# Many Variables to one value
x = y = z = "Nikhil"
print(x,y,z)

Unpacking Collection(extract list or tuple into  variables)
fruit = ["Apple","Orange","Mango"]
x,y,z = fruit
print(x,y,z)

practice problem
x = 10
y = 4
sum = x+y
print(sum)
if sum%2==0:
  print("This is even value")
else:
   print("This is odd number")

python output
x = "Python "
y = "is "
z = "Awesome "
print(x+y+z)
x = 5
y = "Nikhil"
print(x,y)

Global Variable/keyword
x = "Awesome"
def myfun():
    global x
    x = "bad"
myfun()
print("Python is " + x)
# Local Variable
def fun():
    x = "sad"
    print("Python is " + x)
fun()

Python Data Types
x = str("N")
print(x)

Python Number
x = 1
y = 586598745525
z = -132649849
print(type(x))
print(type(y))
print(type(z))

Random
import random
print(random.randrange(1,99))

Python Casting (int,float,string)
x = str(3)
y = str(5.7)
z = str("4")
print(x)
print(y)
print(z)

Python String
print('Nikhil')
print("Nikhil")

a = "Job"
print(a)

a = 'Hello World'
print(a[3])

x = "banana"
print(len(x))

txt = "Nikhil Anil Lokare"
print("Lokare" in txt)

x = "Im Nikhil Anil Lokare"
if "k" in x:
  print("Presnt")
else:
  print("Absent")

txt = "Nikhil Anil Lokare"
print("Komal" not in txt)

Slicing String
a = "Hello World"
print(a[4:8])

Modify String
a = "nikhil"
print(a.split(","))

Concatination String
a = "Nikhil"
b = "Lokare"
c = a+ " " +b
print(c)

Format String(use arguments ,format them and palce them string where the place horder)
age = 58
txt = "My age is {}"
print(txt.format(age))

x = 24
y = 11
z = 1998
birth = "My birthdate is {}, and birthmonth is {}, and my birthyear is {}"
print(birth.format(x,y,z))

Escape Character
x = "Nikhil is the best \"bgmi\" player in the world"
print(x)

txt = "\121\123\943\789\654"
print(txt)

String methods
txt = "nikhil"
x = txt.capitalize()
print(x)

txt = "Nikhil"
x = txt.casefold()
print(x)

txt = "nikhil"
x = txt.center(40)
print(x)

txt = "nikhil"
x = txt.center(40)
print(x)

Python Boolean
print(10>9)
print(10!=0)
print(9>10)

x = 9
y = 8
if 8>9:
  print("x is greater than y")
else:
  print("y is greater than x")

Python Operator
Arithmetic operator
Assignment operator
comparison operator
logical operator
bitwise operator
membership operator
identity operator

Python List
myList = ["Nikhil","Aniket","Sushil","Nikhil"]
print(len(myList))

Access List
x = [1,2,3]
print(x[-1])

Range of index
x = [1,2,3,4,5,6,7]
if 55 in x:
  print("present")
else:
  print("absent")

Change Item List
myList = ["nikhil","aniket","ram","krsna"]
myList[0] = "Arjun"
print(myList)

change the range of item values
myList = ["nikhil","aniket","ram","krsna"]
myList[1:3] = ["Arjun","krishna"]
print(myList)

Insert Item
myList = ["nikhil","aniket","ram","krsna"]
myList.insert(6,"arjun")
print(myList)

Add item in the list
Append() and item end of the list
x = ["Apple","Orange","banana"]
x.append("Mango")
print(x)

Insert
x = ["Apple","Orange","banana"]
x.insert(0,"Mango")
print(x)

Extend()
x = [1,2,3,4,3,4]
y = [5,6,7,8]
x.extend(y)
print(x)

Python remove list item
x = ["Nikhil","Aniket","Suraj","Manoj"]
x.remove("Nikhil")
print(x)

Remove Specified Index
x = [1,2,3,4,5,6]
x.pop()
print(x)

x = [1,2,3,4,5,6]
x.clear()
print(x)

Loops in the list
List = [1,2,3,4,5,6]
for x in range(len(List)):
 print(List[x])

While loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

while loop using comprehension
x = [1,2,3,4,5]
[print(i) for i in x]

List Comprehension
list = ["Nikhil","Aniket","Lokare"]
new = []
for x in list:
  if "a" in x:
    new.append(x)
    print(new)

Sort List
myList = [1,3,5,7,2,4,6]
myList.sort()
print(myList)

Costumize Sort Function
x = ["aniket","Nikhil","bali","Ksrna"]
x.sort(key = str.lower)
print(x)

Reverse Order
myList = [1,3,5,7,2,4,6]
myList.reverse()
print(myList)

Copy List{1 way}
Mylist = [1,2,3,4,5,6,7]
x = Mylist.copy()
print(x)

2 way
m = [1,2,3,4,5]
a = list(m)
print(a)

Join two List
l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(l1 + l2)

l1 = [1,2,3,4]
l2 = [5,6,7,8]
for x in l2:
  l1.append(x)
  print(l1)

x = [1,2,3]
y = [4,5,6]
x.extend(y)
print(x)

List method
append,clear,copy,pop,sort,reverse,insert,index,count,remove,extend

tuple
myTuple = ('Nikhil', 'Aniket', 'Abhi', 'sakshi','Nikhil')
print(len(myTuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

Tuple store string ,int,boolean types of data
tuple = (1,2,3,4,5)
tuple = ('nikhil','aniket','naman')
tuple = (True,False,False,True)

Access Tuple
tuple = ('nikhil','aniket','sanket','priyanka','nikhil')
print(tuple[0])
print(tuple[-1])
print(tuple[2:4])
print(tuple[1:])
print(tuple[:3])
print(tuple[-1:-3])

for x in tuple:
  if "nikhil" in x:
    print("Yes nikhil is present")
  else:
    print("nikhil is not present")

Update Tuples
convert tuple into list
x = ('apple','orange','mango')
y = list(x)
y.remove("orange")
x = tuple(y)
print(x)

Unpack Tuple
fruit = ('apple','mango','banana')
(green, yellow, red) = fruit
print(green)
print(yellow)
print(red)

using asterisk
fruits = ("apple","banana","mango","orange","graps")
(green,*red,yellow) = fruits
print(green)
print(yellow)
print(red)

Loop tuple
tuple = ("apple","mango","orange","banana","graps")
for x in range(len(tuple)):
  print(tuple[x])

while loop
tuple = ("apple","mango","orange","banana","graps")
i=0
while i < len(tuple):
  print(tuple[i])
  i = i+1

join tuple
x = ("apple","banana","mango")
y = ("graps","orange")
print(x+y)

2 way to join tuple
x = ("nikhil","aniket","manoj")
tuple = x * 2
print(tuple)

tuple method(count.index)
x = (1,2,3,4,3,2,1,2,3,4)
tuple = x.count(2)
print(tuple)

index
x = (1,2,3,4,5,6,7)
tuple = x.index(4)
print(tuple)

Python Set(No duplication allowed)
set is  a collection which is unordered,unchangable,unindexed

myset1 = {"apple", "banana", "mango"}
myset2= {1,2,3,4,5,6,7}
myset3 = {True,False,True}
print(type(myset3))

myset5 = set(("apple","banana","mango"))
print(myset5)

Access Items
i = {"apple", "banana", "mango"}
print("banana" in i)

i = {"apple", "banana", "mango"}
for x in i:
 print(x)

Add items
x = {'nikhil','aniket','sanket'}
x.add("avinash")
print(x)

x = {1,2,3,4,5,6}
y = {7,8,9}
x.update(y)
print(x)

set = {1,2,3,4,5}
list =  [6,7,8,9,1]
set.update(list)
print(set)

Remove Set Items
myset = {1, 2, 3, 4, 5}
myset.remove(3)
print(myset)
# Discard
myset = {1, 2, 3, 4, 5}
myset.discard(5)
print(myset)
pop()
myset = {1, 2, 3, 4, 5}
x = myset.discard(5)
print(x)
print(myset)

Loop Items
my = {1,2,3,4,5}
for x in my:
  print(my)

Join Sets
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = set1.union(set2)
print(set3)

set1 = {'a','b','c'}
set2 = {1,2,3}
set1.update(set2)
print(set1)

Kepp only the duplicates
x = {'apple','mango','banana'}
y = {'google','uber','apple'}

z = x.intersection(y)
print(z)

keep all but not duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

Set Methods
add,clear,copy,intersection,difference,
pop,remove,discard,union,update

Python Dictionaries
dict = {
  "brand":"ford",
  "model":"mustang",
  "year":1998,
  "color":['red','orange','blue']
}
print(dict)
print(dict)
print(len(dict))
print(type(dict))
print(type(dict))

Access Items in Dict
dict = {
  "brand":"ford",
  "model":"mustang",
  "year":1998,
  "color":['red','orange','blue']
}
x = dict.get("year")
x = dict["model"]
print(dict.values())
print(dict.keys())
x = dict.keys()
print(x)
dict["engine"] = "purple"
print(x)

x = dict.items()
print(x)
dict["tyre"] = "MRF"
print(x)

dict.update({"brand":"Toyoto"})
print(dict)

dict["color"] = "blue"
print(dict)

Remove items
dict.clear()
print(dict)

for x in dict:
  print(x)
for x in dict:
  print(dict[x])
for x in dict.values():
  print(x)
for x in dict.keys():
  print(x)
for x,y in dict.items():
  print(x,y)

Copy Dict
mydict = dict.copy()
print(mydict)
mydict = dict(dict1)
print(mydict)

Nested Dict
myfamily = {
  "child1":{
    "name":"Nikhil",
    "age":21
  },
  "child2":{
    "name":"ANiket",
    "age":24
  },
  "child3":{
    "name":"Ankush",
    "age":13
  }
}
print(myfamily)

child1 = {
    "name":"Nikhil",
    "age":21
  },
child2={
    "name":"ANiket",
    "age":24
  },
child3={
    "name":"Ankush",
    "age":13
  }
myfamily={
  "child1":child1,
  "child2":child2,
  "child3":child3,

}
print(myfamily)

dict methods
clear,copy,fromkeys,get,items,keys,pop,
popitem,setdefault,updae,values

If Statement
a = 44
b = 99
if a < b:
  print("greater")

Elif
a = 33
b = 44
if b>a:
  print("b is greater than a")
elif a==b:
  print("a and b are equal")

else
a = 33
b = 44
if b>a:
  print("b is greater than a")
elif a==b:
  print("a and b are equal")
else:
  print("a is greater tha b")

short hand
a  =6
b = 9
print("true") if a > b else print("false")

And
a = 3
b = 4
c = 7

if a < b and c > b:
  print("Both are true")
else:
  print("false")

# pass statement
a = 33
b = 200

if b < a:
  pass

While Loop
i = 0
while i<6:
  i +=1
  if i==3:
    continue
  print(i)

For Loop
simple for loop
x = ['apple','banana','mango']
for i in x:
  print(i)

Break statement
for i in x:
  if i =='banana':
    break
  print(i)

Continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

Range in loop
for x in range(9): print(x)
for x in range(2,8): print(x)
for x in range(2,50,2): print(x)

Else in For Loop
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally Finished")

Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

Pass the statement
for x in [0,1,2]:
  pass

Functions in Python
def my_function():
  print("hello from the function")

my_function()

Argument
def my_function(fname,mname,lname):
  print(fname + mname + lname )

my_function("Nikhil ","Anil ","Lokare")
my_function("Aniket ","Anil ","Lokare")

Arbitrary *args
def my_function(*kids):
  print(kids[0] + " is good boy")

my_function("Nikhil","Aniket","omkar")

Key Argument

def my_function(c1,c2,c3):
  print("Smasher " + c2)

my_function(c1 = "Nikhil",c2="Aniket",
             c3="Suhas")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

Default Parameter
def my_function(country="Norway"):
  print("I am from " + country)

my_function("mumbai")
my_function("swedan")
my_function()
my_function()
my_function("sydney")

Passing List of An argument
def my_function(food):
  for x in food:
    print(x)

number = [1,2,3,4,5]

my_function(number)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(4))
print(my_function(5))

pass the statement
def my_function():
   pass

recurssion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)

Python Lambda

x = lambda a , b , c: a + b + c
print(x(4,7,6))

Python Array === List

Python Classes And Objects
its object oriented programming language

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

the_init_()Function (Constructure)

class person:
  def __init__(self,name,age,email):
    self.name = name
    self.age = age
    self.email = email

p1 = person("Nikhil",25,"nikhil@.com")

print(p1.name)
print(p1.age)
print(p1.email)

__str__() function
class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = person("Nikhil",25)

print(p1)

Object Methods
class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("My Name is " + self.name)

p1 = person("Nikhil",25)
p1.myfunc()

Self Parameter
class Person:
  def __init__(abc,name,age):
    abc.name = name
    abc.age = age

  def myfunc(xyz):
    print("My Name is " + xyz.name)

p1 = Person("Nikhil", 25)
p1.myfunc()

Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)

Python Inheritance
parent class
class Person:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

  def func(self):
      print(self.fname,self.lname)

x = Person("Nikhil","Lokare")
x.func()

# Child Class
class Student(Person):
  def __init__(self,fname,lname):
    super().__init__(self,fname,lname)

x = Student("Aniket","Lokare")
x.func()

Super() function keyword in python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname,self.lastname, "to the class of ", self.graduationyear)
x = Student("Nikhil","Lokare",2021)
x.welcome()

Python Syntex
class BaseClass:
  {body}
class derivedClass(BaseClass):
  {body}

Iterators
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

my = "Banana"
for x in my:
  print(x)

Scope in python

def func():
  x = 300
  def nik():
    print(x)
    def aniket():
      print(x)
      aniket()

  nik()

func()

def my():
  print(x)

my()

global variable

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

x = 300
def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

def myfunc():
  global x
  x = 300
  print(x)
myfunc()

print(x)
print(x)
print(x)

x = 300
def myfunc():
  global x
  x = 200

myfunc()
print(x)

import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

Python Math
x = min(1,2,3)
y = max(4,5,6)

print(x)
print(y)

x = abs(-5)
print(x)

x = pow(4,3)
print(x)

import math

x = math.sqrt(24)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

x = math.pi
print(x)

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
