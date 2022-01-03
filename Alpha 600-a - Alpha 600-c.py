
'''              بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ            '''


'''Alpha 600a - 600c'''

"""Exception handling  """


try: 
    1/0
except ZeroDivisionError:
    print("you cannot divide by zero")


print("-----------------------------------")


my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    }

try: 
    value = my_dict['d']
except KeyError:
    print("The key is invalid")
finally:
    print("this dict is executed")
  
print("-----------------------------------")

  
my_list = [1,2,3,4,5,6]

try:
    my_list[2]
except IndexError:
    print("this index is not a value list index")
else:
    print("No error occured ")


print("-----------------------------------")

