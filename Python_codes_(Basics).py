Section 2: Python Introduction

8. Our First Python Program                                   

print('Vivek Negi')                                   Vivek Negi
                                 
input('what is your name?')                           what is your name?Vivek

Name = input('what is your name?')
print(Name)                                           what is your name?Vivek

Name = input('what is your name?')                   
print('hello' + Name)                                 what is your name?vivek
                                                      hello vivek


9. Latest Version Of Python   

Python Documentation link- https://docs.python.org/3/


Section 3: Python Basics

17. Python Data Types

Fundamental Data types
int
float
bool
str
list
tuple
set
dict

Classes <- Custom data types
where we create our own datatypes

Specialized Data types
where we use data types from large libraries

None
Nothing

19. Numbers

int - Numbers without decimal
float - Numbers with decimal

#int
example- 2, 3, 4 , 5

print(2 + 4)               6
print(2 - 4)              -2
print(2 * 4)               8
print(2 / 4)               0.5

print(type(6))             int
print(type(2 - 4))         int
print(type(2 * 4))         int
print(type(2 / 4))         float
.
print(2 ** 3)
Means 2 the power 3

print(2 // 3)
round off the number.

print(5 % 3)
magilo sign give the reminder

20. Math Functions

round- round off the number
abs- convert the negative no into postive

print(round(2.6))         3
print(abs(-3))            3



23. Exercise: Operator Precedence

Excercise

print((5 + 4) * 10 / 2)       45.0

print(((5 + 4) * 10) / 2)     45.0
  
print((5 + 4) * (10 / 2))     45.0

print(5 + (4 * 10) / 2)       25.0

print(5 + 4 * 10 // 2)        25


24. Optional: bin() and complex

bin = It gives the binary representation of numbers

print(bin(5)    0b101


Now, get to binary to integer/decimal no

print(bin(5)             0b101
print(int('0b101', 2)    5

note:- 2 = base
binary represents a number in base 2 (0 and 1)
octal represents a number in base 8 (0, 1, 2, 3, 4, 5, 6 and 7)
decimal is what is used in daily (western) life to talk about integers, which is base 10 (0 through to 9).
hexadecimal is base 16 (0 through to 9, then A, B, C, D, E, F).



25. Variables

program = program is simply data, that can be stored, change and remove.

variables = variables store informattion.


iq = 190
print(iq)    190


Python keywords- https://www.w3schools.com/python/python_ref_keywords.asp

note-
keyword always in blue colour.
example- print()


Constants- The value which never change. It is good to name constants variable name in capital letters.

example- 

PI = 3.14

Dunder- Start with double underscore.

example- __name

varible should not be start with dunder or double underscore.


a,b,c = 1,2,3

print(a)     1
print(b)     2
print(c)     3


26. Expressions vs Statements
 
iq = 100
user_age = iq/5

expression = iq/5 (expression is a piece of code that produces a value.)
statement = user_age = iq/5, iq = 100 (whatever write in codes is called statements).
action = we are dividing iq by 5 and saving it into user_age.

27. Augmented Assignment Operator

some_value = 5

if we have to add, minus, multiply or substract the no then normally we do is,

some_value = 5 + 2
or 
some_value = 5
some_value = (some_value + 2)
print(some_value)                 7


Same thing do with Augmented Assignment Operator.

some_value = 5
some_value += 2
print(some_value)    7


28. Strings

String is a piece of text. In single or double quotes you can't use multiple line for strings.

username = 'supercoder'
password = 'supers'

Long String = Long string should be between triple quotes('''    '''). In triple quotes you can use multiple line for strings.

long_string = '''
wow
O O
---
'''
print(long_string)          wow
                            O O
                            ---


first_name = 'vivek'
last_name = 'negi'
full_name = first_name + last_name
print(full_name)                                     viveknegi

For space between first and last name in output,

first_name = 'vivek'
last_name = ' negi'
full_name = first_name + last_name
print(full_name)                                     vivek negi


or

first_name = 'vivek'
last_name = 'negi'
full_name = first_name + ' ' + last_name
print(full_name)                                      viveknegi





29. String Concatenation 


String Concatenation means adding string together. It only works with strings.

print('vivek' + 'negi')          viveknegi
print('vivek' + ' negi')         viveknegi

print('vivek' + 5)               error


30. Type Conversion

print(str('100'))                      100
print(type(str('100')))                <class 'str'>
print(type(int(str('100'))))           <class 'int'>


a = str('100')
b = int(a)
c = type(b)
print(c)                               <class 'int'> 



31. Escape Sequences

weather = 'It's a "kind of" sunny'             
print(weather)                                                              error

weather = 'It\'s a \"kind of\" sunny'      
print(weather)                                                              It's a "kind of" sunny


tab (\t) (Space)- It will gives the spacing after \t.

weather = '\t It\'s a \"kind of\" sunny'
print(weather)                                                                It's a "kind of" sunny

New Line (\n)- It will bering a new line.

weather = '\t It\'s a \"kind of\" sunny \n hope you will be fine'          
print(weather)                                                                It's a "kind of" sunny 
                                                                            hope you will be fine




32. Formatted Strings

name = 'Vivek'
print name with greet
print('hello ' + name)                                                      hello Vivek


name = 'Vivek'
age = 23
print('hello ' + name + '. You are ' + str(age) + ' year old.')             hello Vivek. You are 23 year old.

Formatted string(f)= Using f in beginning of the sentence.

name = 'Vivek'
age = 23
print(f'hello {name}. You are {age} year old.)                              hello Vivek. You are 23 year old. 

or

print('hello {}. You are {} year old.'.format('Vivek', '23'))               hello Vivek. You are 23 year old. 

note:- It will fill bracket in order.

or

name = 'Vivek'
age = 23
print('hello {}. You are {} year old.'.format(name, age))                   hello Vivek. You are 23 year old. 

note:- It will not follow the order beacause we are using 
variables names(name, age).

or 

name = 'Vivek'
age = 23
print('hello {1}. You are {0} year old.'.format(name, age))                 hello 23. You are Vivek year old.
note:- We can also use indexing to select the order.

or

print('hello {new_name}. You are {age} year old.'.format                    
(new_name = 'kamaric', age = 23))                                          hello kamaric. You are 23 year old.

note:- We can also change the values of variables.


33. String Indexes

String Indexes help in access of different part of string.

Name = 'Vivek Negi'              
print(Name[4])                   k  

Negative Index: It means start from back.

Name = 'Vivek Negi'
print(Name[-1])                  i                   
 
Stop

Use colon(:) in indexing. Colon(:) tell, where to start and where stop.

example: [Start:Stop]

Name = 'Vivek Negi'
print(Name[0:9])                Vivek Neg

Name = 'Vivek Negi'
print(Name[1:])                  ivek Negi

Name = 'Vivek Negi'
print(Name[:5])                  Vivek


Stepover

example- [Start:Stop:Stepover]

Name = 'Vivek Negi'
print(Name[0:9:2])               VvkNg

Name = 'Vivek Negi'
print(Name[::1])                 Vivek Negi

Name = 'Vivek Negi'
print(Name[::-1])                igeN keviV


Excercise

Name = 'I am PYHTON'
print(Name[2:4])             am
print(Name[2:])              am PYHTON
print(Name[0:])              I am PYHTON
print(Name[2:11])            am PYHTON
print(Name[-1])              N
print(Name[-4])              H
print(Name[:8])              I am PYH
print(Name[8:])              TON
print(Name[::-1])            NOTHYP ma I





34. Immutability

It means, you can't change the part of values.

value = '12345'
value[0] = '2'
print(value)                  error


35. Built-In Functions + Methods

print(len('hellloooo'))             9

greet = 'hellloooo'
print(greet[0:len(greet)])          hellloooo


Difference b/w function and methods?
Answer- Methods are similiar to function but it's only work with strings and always start with dot(.)
for example:- .format

quote = 'to be or not to be'
print(quote.upper())              TO BE OR NOT TO BE

note- It's convert sentence from lower case to upper case.


quote = 'to be or not to be'
print(quote.capitalize())         To be or not to be

note- It's capitalize the first alphabet of the sentence.

quote = 'to be or not to be'
print(quote.find('be'))             3

note- It's give the starting index of the word which you are finding. 

quote = 'to be or not to be'
print(quote.lower())               to be or not to be

note- It's convert sentence from upper case to lower case.

quote = 'to be or not to be'
print(quote.replace('be', 'me'))        to me or not to me

note- It's replace a be with me.


quote = 'to be or not to be'
print(quote.replace('be', 'me'))       to me or not to me
print(quote)                           to be or not to be

note- Even we are replacing a be with me but the orgina value(value assign first time) of quote will remain same because strings are immutable(we can change the part of string).

Built in fuctions link- https://docs.python.org/3/library/functions.html
python string methods link- https://www.w3schools.com/python/python_ref_string.asp



36. Booleans

Booleans are logical values like true, false. It represent with bool.

print(bool(0))      False
print(bool(1))      True


37. Exercise: Type Conversion

birth_year = input('what year were you born?')
age = 2021 - int(birth_year)
print(f'your age is: {age}')                          what year were you born?1997
                                                      your age is: 24




38. DEVELOPER FUNDAMENTALS: II

Article:- https://realpython.com/python-comments-guide/


39. Exercise: Password Checker

username = input('what is your username?')
password = input('what is your password?')
print(f'Your username is {username}, Your password is 
{password} and it is {len(password)} letter long')             what is your username?vivek
                                                               what is your password?123456789
                                                               Your username is vivek, Your password is 123456789 
                                                               and it is 9 letter long


Hide the password

username = input('what is your username?')
password = input('what is your password?')
password_lenth = len(password)
hidden_password = '*' * password_lenth
print(f'Your username is {username}, Your password is 
{hidden_password} and it is {len(password)} letter long')      what is your username?vivek
                                                               what is your password?123456789
                                                               Your username is vivek, Your password is ********* 
                                                               and it is 9 letter long



40. Lists

It is order sequence of object, which can be anytype.

li = [1,2,3,4]
li1 = ['a', 'b', 'c']
li2 = [1,2, 'a', True]

Data Structure- It is way for us to organize information and data into the folder.


41. List Slicing

amazon_cart = [
'notebooks', 
'sunglasses', 
'toys', 'grapes'
] 
print(amazon_cart)            ['notebooks', 'sunglasses', 'toys', 'grapes']



List is mutable. Means we can change the part of list.

amazon_cart = [
'notebooks', 
'sunglasses', 
'toys', 'grapes'
] 
amazon_cart[0] = 'laptops'
print(amazon_cart)             ['laptops', 'sunglasses', 'toys', 'grapes']




amazon_cart = ['notebooks', 
'sunglasses', 
'toys', 
'grapes']
amazon_cart[0] = 'laptops'
print(amazon_cart[0:3])           ['laptops', 'sunglasses', 'toys']
print(amazon_cart)                ['laptops', 'sunglasses', 'toys', 'grapes']

                     

amazon_cart = ['notebooks', 
'sunglasses', 
'toys', 
'grapes'
]
amazon_cart[0] = 'laptops'
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)                  ['gum', 'sunglasses', 'toys']
print(amazon_cart)               ['laptops', 'sunglasses', 'toys', 'grapes']



amazon_cart = [
'notebooks', 
'sunglasses', 
'toys', 
'grapes'
]
amazon_cart[0] = 'laptops'
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)                  ['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart)               ['gum', 'sunglasses', 'toys', 'grapes']


amazon_cart = [
'notebooks', 
'sunglasses', 
'toys', 
'grapes'
]
amazon_cart[0] = 'laptops'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)                  ['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart)               ['laptops', 'sunglasses', 'toys', 'grapes']


Excercise

new_list = ['a', 'b', 'c']
print(new_list[1])                  b
print(new_list[-2])                 b
new_list[0] = 'z'
print(new_list)                     ['z', 'b', 'c']
no_list = [1,2,3,5]
mix_list = no_list[0:3]
mix_list[0] = 'z'
print(mix_list)                     ['z', 2, 3]
print(no_list)                      [1, 2, 3, 5]


42. Matrix


How to access value in multidemensional metrix:

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[1][1])                    5  




Excercise

# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

print(basket[1][1])                                                     "Oranges"
or
basket[1][1][0]                                                         "Oranges"    



43. List Methods

basket = [1,2,3,4,5]

Adding Method- 

.append- Append help in to add value in last.

basket = [1,2,3,4,5]
new_list = basket.append(100)
print(new_list)                                none
print(basket)                                  [1, 2, 3, 4, 5, 100]

note- The out put is none because when we do append it doesn't produce in new list(new varaibale). It changes or update is origanal list(assign values in first time in which variable).

For bring changes in new list or new variable, we have to do like this-


basket = [1,2,3,4,5]
basket.append(100)
new_list = basket
print(new_list)               [1, 2, 3, 4, 5, 100]

.insert- Insert help in add value in list 'anywhere you want to add' through indexing.


basket = [1,2,3,4,5]
new_list = basket.insert(4, 100)
print(new_list)                     none
print(basket)                       [1, 2, 3, 4, 100, 5]

Note- None because it doesn't produce new list it would make changes only in the list.

basket = [1,2,3,4,5]
basket.insert(4, 100)
new_list = basket
print(new_list)                 [1, 2, 3, 4, 100, 5]
print(basket)                   [1, 2, 3, 4, 100, 5]



.extend- Extend help in to add list in the old list from end.

basket = [1,2,3,4,5]
new_list = basket.extend([4, 100])
print(new_list)                      None
print(basket)                        [1, 2, 3, 4, 5, 4, 100]


 
basket = [1,2,3,4,5]
basket.extend([4, 100])
new_list = basket
print(new_list)                     [1, 2, 3, 4, 5, 4, 100]
print(basket)                       [1, 2, 3, 4, 5, 4, 100]


Removing Method

.pop = It will remove the value from the end and also we can use indexes to remove value.               

basket = [1,2,3,4,5]
basket.pop()
print(basket)                       [1, 2, 3,4] 


remove with help of index

basket = [1,2,3,4,5]
basket.pop(3)
print(basket)                      [1, 2, 3, 5]


basket = [1,2,3,4,5]
new_list = basket.pop(4)
print(new_list)                     5

note- It doesn't gives none because different method work differently.


.remove- In this method, we don't remove value through indexing, we just put value that we want to remove.

basket = [1,2,3,4,5]
basket.remove(3)
print(basket)                     [1, 2, 4, 5]


.clear- In this method, we can clear all value in the list.

basket = [1,2,3,4,5]
basket.clear()
print(basket)                     []  


basket = [1,2,3,4,5]
basket.clear(2)
print(basket)                   error  (error because of this basket.clear(2). .clear doesn't take any argument(2).)




List methods link- https://www.w3schools.com/python/python_ref_list.asp


44. List Methods 2


.index- It help in find the index no value.

basket = [1,2,3,4,5]
print(basket.index(2))                  1


basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d'))                  3


basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d', 0, 4))           3


keywords

in

basket = ['a', 'b', 'c', 'd', 'e']
print('d' in basket)                        True


basket = ['a', 'b', 'c', 'd', 'e']
print('f' in basket)                        False


print('my' in 'my name is vivek')           True


.count- It count that how many time item occur.

basket = ['a', 'b', 'c', 'd', 'e']
print(basket.count('d'))                   1

python keywords link- https://www.w3schools.com/python/python_ref_keywords.asp


Excercise

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket

print(basket)

Solution:-

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.pop(2)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))                                    2
print(basket)                                                    ['Apples', 'Apples', 'Oranges', 'Kiwi']
basket.clear()                                                  
print(basket)                                                    []                                                                                              


45. List Methods 3

.sort

basket = ['a', 'x', 'b', 'c', 'd', 'e']
print(basket.sort())                          None

note- It doesn't produce anything that's why is giving none. It's only make change in place.

basket = ['a', 'x', 'b', 'c', 'd', 'e']
(basket.sort())
print(basket)                                 ['a', 'b', 'c', 'd', 'e', 'x']


sorted function

basket = ['a', 'x', 'b', 'c', 'd', 'e']
print(sorted(basket)                     ['a', 'b', 'c', 'd', 'e', 'x']                    
print(basket)                            ['a', 'x', 'b', 'c', 'd', 'e']

note- why it has not change basket or update the basket because we just only printed the basket not save the change . But when we use .sort method then it change or update the place.

                 
basket = ['a', 'x', 'b', 'c', 'd', 'e']
new_basket = basket[:]
new_basket.sort()
print(new_basket)                       ['a', 'b', 'c', 'd', 'e', 'x']
print(basket)                           ['a', 'x', 'b', 'c', 'd', 'e']


.copy- It copy the list.

basket = ['a', 'x', 'b', 'c', 'd', 'e']
new_basket = basket[:]
new_basket.copy()
print(new_basket)                       ['a', 'x', 'b', 'c', 'd', 'e']
print(basket)                           ['a', 'x', 'b', 'c', 'd', 'e']


.reverse- It reverse the list.

basket = ['a', 'x', 'b', 'c', 'd', 'e']
basket.reverse()
print(basket)                           ['e', 'd', 'c', 'b', 'x', 'a']


sort(.sort) + reverse(.reverse)

basket = ['a', 'x', 'b', 'c', 'd', 'e']
basket.sort()
basket.reverse()
print(basket)                           ['x', 'e', 'd', 'c', 'b', 'a']



46. Common List Patterns


basket = ['a', 'x', 'b', 'c', 'd', 'e']
basket.sort()
basket.reverse()
print(basket[::-1])                    ['a', 'b', 'c', 'd', 'e', 'x']
print(basket)                          ['x', 'e', 'd', 'c', 'b', 'a']


Range- 
example- range(start, stop, stepover)

print(range(1, 100))                   range(1, 100)
print(list(range(1, 100)))             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,                                        35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,                                        67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,                                        99]


print(list(range(11)))                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


.join- It usually work with strings. It join the two strings.

sentence = ' ' 
new_sentence = sentence.join(['my' 'name' 'is' 'vivek' 'negi'])
print(new_sentence)                                                   mynameisviveknegi


new_sentence = ' '.join(['my' 'name' 'is' 'vivek' 'negi'])
print(new_sentence)                                                   mynameisviveknegi







47. List Unpacking

a,b,c = [1,2,3]
print(a)               1
print(b)               2
print(c)               3


a,b,c, *duo = [1,2,3,4,5,6,7,8,9]
print(a)               1
print(b)               2
print(c)               3
print(duo)             [4, 5, 6, 7, 8]

a,b,c, *duo,d = [1,2,3,4,5,6,7,8,9]
print(a)               1
print(b)               2
print(c)               3
print(duo)             [4, 5, 6, 7, 8]
print(d)               9

48. None

It is null value.

weapons = None
print(weapons)      None


50. Dictionaries

Dictionary is unorder key value pair. Unorder means keys under dictionary could be anywere in the memory. It's not like 'List'. list is in order way.

dictionary = {
  'a' : 1,
  'b' : 2,
  'c' : 3
}
print(dictionary['a'])                        1
print(dictionary)                             {'a': 1, 'b': 2, 'c': 3}


dictionary = {
  'a' : [1,2,3],
  'b' : 'hello',
  'c' : True
}

print(dictionary['a'])                  [1,2,3]
print(dictionary['a'][1])               [2]



my_list = [
  {
  'a' : [1,2,3],
  'b' : 'hello',
  'x' : True
},
{
  'a' : [4,5,6],
  'b' : 'hello',
  'x' : True
}
]
print(my_list[0]['a'][2])            3




51. DEVELOPER FUNDAMENTALS: III
 
Difference between List and Dictionary?

List follow order Dictionary doesn't follow order.


52. Dictionary Keys

dictionary = {
  'weapons'  : [1,2,3],
  'greeting': 'hello',
  'is_magic' : True
}

dictionary = {
  '123' : [1,2,3],
  True : 'hello',
  'is_magic' : True
}
print(dictionary[123])             [1,2,3]
print(dictionary[True])            hello


dictionary = {
  '123'  : [1,2,3],
  True : 'hello',
  [100] : True                    error(TypeError: unhashable type: 'list')
}
key should be immutable that's mean it can't be change
Key has to be unique in the dictionary.


dictionary = {
  '123'  : [1,2,3],
  '123' : 'hello'
}
print(dictionary['123'])        hello

note- If keys are not unique then the last key value ovewrite the previous key value.


53. Dictionary Methods

user = {
  '123'  : [1,2,3],
  'greet' : 'hello'
}
print(user['age'])           error


Method

.get- In generally, we don like to see error. So, dot get(.get) help us in doesn,t show the error. It will show none, if we will use .get.


user = {
  '123'  : [1,2,3],
  'greet' : 'hello'
}
print(user.get('age'))      None


Default value- if age is not in the user(dictionary) then by .get you can get default value of age.



user = {
  '123'  : [1,2,3],
  'greet' : 'hello'
}
print(user.get('age', 23))      23


if suppose we have a age key in user(dictionary),


user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print(user.get('age', 23))      20


Another way of creating dictionary which is not common

user2 = dict(name = 'Vivek Negi')
print(user2)                             {'name': 'Vivek Negi'}


Dictionary Methods Link- https://www.w3schools.com/python/python_ref_dictionary.asp
 

54. Dictionary Methods 2

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}

print('size' in user)      False


.keys- Check the key in user(dictionary)

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print('age' in user.keys())      True



.values- Check the value in user(dictionary)

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print('hello' in user.values())        True


.item- It print the all keys with value in the dictionary.

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print(user.items())       dict_items([('123', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])



.clear- Empty dictionary.

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print(user.clear())      None  

or

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
user.clear()
print(user)               {}
 
 
.copy- copy the dictionary into new varibale.

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
user2 = user.copy()
print(user2)               {'123': [1, 2, 3], 'greet': 'hello', 'age': 20}


.pop- .pop remove or return the value which you remove.

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print(user.pop('age'))           20
print(user)                      {'123': [1, 2, 3], 'greet': 'hello'}


.popitem- The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}
print(user.popitem())      ('age', 20)    
print(user)                {'123': [1, 2, 3], 'greet': 'hello'}



.update- The update() method inserts the specified items to the dictionary.

user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}

user.update({'age' : 23})
print(user)                                {'123': [1, 2, 3], 'greet': 'hello', 'age': 23}



user = {
  '123'  : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}

user.update({'subject' : 'analytics'})
print(user)                               {'123': [1, 2, 3], 'greet': 'hello', 'age': 20, 'subject': 'analytics'}

 

55. Tuples

Tuples

Tuples is like list but unlike list we can't modify it. There are immutable. a tupple is immutable. Once you create it, You can't sort it or reverse it like we saw with lists. It's just there.


It makes your code safer because people can modify right it makes code more predictable.

It makes code more predictable but it's less flexible than a list.

I can't really sort a tuple or I can't run reverse on topple now because of this because they are less

flexible.

The other good thing about them is that they're slightly more performance than lists so they're usually

Faster than lists and if you don't need a list to change we'll use a couple.





my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z'                    error

note- Output is error because tuple is immutable. You can't change, sort and reverse the Tuple.


my_tuple = (1,2,3,4,5)
print(my_tuple[1])                  2


my_tuple = (1,2,3,4,5)
print(5 in my_tuple)                True


user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}                                       
print(user.items())                 dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])


user = {
  (1,2): [1,2,3],
  'greet': 'hello',
  'age': 20
}                         
print(user[(1,2)])                  [1,2,3]


56. Tuples 2

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]
print(new_tuple)                    (2,)


my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]
print(new_tuple)                    (2, 3, 4)




my_tuple = (1,2,3,4,5)
x = my_tuple[0]
y = my_tuple[1]
z = my_tuple[2]
others = my_tuple[3:]
print(x)                            1
print(y)                            2
print(z)                            3
print(others)                       4, 5 

or
        

x, y, z, * others = (1,2,3,4,5)
print(x)                            1
print(y)                            2
print(z)                            3
print(others)                       4, 5
         

Tuple methods-

count()- Returns the number of times a specified value occurs in a tuple.


my_tuple = (1,2,3,4,5,5)
print(my_tuple.count(5))           2

index()- Searches the tuple for a specified value and returns the position of where it was found

my_tuple = (1,2,3,4,5) 
print(my_tuple.index(5))           4

my_tuple = (1,2,3,4,5) 
print(len(my_tuple))               5


                                     
57. Sets                                    

Set- Set is an unordered collection of unique objects.

my_set= {1,2,3,4,5,5} 
print(my_set)                    {1, 2, 3, 4, 5}

note- It only returns the unique sets or unique items you see in a set. There's no duplicates. Everything has to be unique. So, this fire just never gets added to a set.


Methods-

.add()- We can add new values into set by .add() method.

my_set= {1,2,3,4,5} 
my_set.add(100)
my_set.add(2)
print(my_set)                    {1, 2, 3, 4, 5, 100}

note- 100 added in the set but not 2 because 2 is already in the set.


Covert the List into set:-

my_set= [1,2,2,3,4,5,5] 
print(set(my_set))               {1, 2, 3, 4, 5}


note- When would this be useful.

Imagine, if we had user names right or email addresses where collecting email addresses on our startup page. But we don't want to have duplicate emails. We might want to convert this a list of emails to a set and remove any duplicates. So we're not sending emails over and over.


Accessing with Index numbers:-

my_set = {1,2,3,4,5,5} 
print(my_set[0])                 error

note- Set doesn't support Indexing. In order to access a set, We have to grab by the item that's in it.


Access the set-

my_set = {1,2,3,4,5,5} 
print(1 in my_set)               True


my_set = {1,2,3,4,5,5} 
print(len(my_set))               5

note- It only counts the unique things because this will never gets entered.


we can also convert set into a list.

my_set = {1,2,3,4,5,5} 
print(list(my_set))             [1, 2, 3, 4, 5]


Set methods-

.copy()- It's help in to creat the duplicate of set.

my_set = {1,2,3,4,5,5} 
new_set = my_set.copy()
print(new_set)                  {1, 2, 3, 4, 5}

.clear()- It's help in to clear the set.

my_set = {1,2,3,4,5,5} 
new_set = my_set.copy()
my_set.clear()
print(my_set)                    set()


58. Sets 2

Set Methods

.difference()- Returns a set containing the difference between two or more sets.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.difference(your_set))                     {1, 2, 3}


.discard()- Remove the specified item.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
my_set.discard(5)
print(my_set)                                          {1, 2, 3, 4}


.difference_update()- Removes the items in this set that are also included in another, specified set.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.difference(your_set))                      {1, 2, 3}
print(my_set)                                           {1, 2, 3, 4, 5}

note- .difference() didn't update in my_set variable. So, in that case, we will use .difference_update().

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set)                                           {1, 2, 3}


.intersection()	Returns a set, that is the intersection of two other sets.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.intersection(your_set))                    {4, 5}

or

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set & your_set)                                {4, 5}

.isdisjoint()	Returns whether two sets have a intersection or not.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.isdisjoint(your_set))                      False


.issubset()	Returns whether another set contains this set or not.

my_set = {4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.issubset(your_set))                        True

.issuperset()	Returns whether this set contains another set or not. 

my_set = {4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.issuperset(your_set))                      False


.union()	Return a set containing the union of sets but remove duplicates.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10} 
print(my_set.union(your_set))                           {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

or

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set | your_set)                                {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}






Section 4: Python Basics II

is_old = True
is_licenced = True

if is_old: 
  print('You are old enough to drive!')                You are old enough to drive!
else:
  print('checkcheck')                                            



is_old = False
is_licenced = True

if is_old: 
  print('You are old enough to drive!')
else:
  print('checkcheck')                                 checkcheck




              
 


























    
                                                         