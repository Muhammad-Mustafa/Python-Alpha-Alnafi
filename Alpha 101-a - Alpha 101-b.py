# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' Alnafi python Alpha slide code and practice '''

# the code is starting form python Alpha 101-a

'''              بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ            '''


'''Alpha 101-a - Alpha 101-b'''

my_string = 'Welcome to python!'

another_string = "The bright red fox jumped the fence."

a_long_string = '''This is a 
multi-line sting.
It covers more than one line.'''

my_String = "I'm a programmer!"
otherStrings = 'The word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""

print(my_string)
print(another_string)
print(a_long_string)
print(my_String)
print(otherStrings)
print(tripleString)


#str casting 

my_number = 123

print(type(my_number))
print(my_number)

my_number_cast  = str(my_number)

print(type(my_number_cast))
print(my_number_cast)

#string concatenation 

string_1 = "sharfoo is a good"
string_2 = ' guy'
string_3 = string_1 + string_2
print(string_3)

#upper and lower methods in string

str_1 = 'This is a string'
print(str_1.upper())
print(str_1.lower())

#dir in string

print(dir(str_1))

#help in python

print(help(my_string.upper))

#string slicing 

country_name = 'My country name is Pakistan '

print(country_name[0:0])
print(country_name[0:-3])