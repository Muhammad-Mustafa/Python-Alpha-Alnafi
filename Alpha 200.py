#''' Alnafi python Alpha slide code and practice '''

# the code is starting form python Alpha 101-a

'''              بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ            '''


'''Alpha 200'''
'''List'''
my_list = [1,2,3]
my_list1 = ["a","b", "c"]
my_list2 = ['a', 1, "Python", 5]
my_nested_list = [my_list,my_list1,my_list2]

combo_list = []
one_list = [4,5]
combo_list.extend(one_list)

new_combo_list = []
new_combo_list.extend(my_list)
new_combo_list.extend(my_list1)
new_combo_list.extend(my_list2)

new_combo_list1 = my_list+my_list1+my_list2

print(my_list)
print(my_list1)
print(my_list2)
print(my_nested_list)
print(combo_list)
print(new_combo_list)
print(new_combo_list1)


print("-----------------------------------")


# Sorting the list using sorting method

alpha_list = [22,3,44,5,66,73,2,-6,0.2,0,1.1,998]
beta_list = [22,3,44,5,66,73,2,-6,0.2,0,1.1,998]
gamma_list = beta_list.sort()

print(gamma_list)

print("-----------------------------------")


print("Before sorting")
print(alpha_list)
print("After sorting")
alpha_list.sort()

print(alpha_list)

print("-----------------------------------")


# Slicing a list 

list_1 = [22,3,44,5,66,73,2,-6,0.2,0,1.1,998]
print(list_1[0:3])

print("-----------------------------------")



'''Tuples'''

my_tuple = (1,2,3,4)
print(my_tuple)

tem_list = [1,2,3.4,55]
tuple_list = tuple(tem_list)

print(tem_list)
print(type(tem_list))
print(tuple_list)
print(type(tuple_list))

tuple_to_list = list(tuple_list)
print(tuple_to_list)
print(type(tuple_to_list))

print("-----------------------------------")


'''Dictionary'''

dict_1 = {
    "one": 1,
    "two": 2,
    "Three": 3
    }

print(type(dict_1))
print(dict_1)

print("-----------------------------------")


address_book = {
    "name":"Mustafa",
    "address": "abc - xyz 123"
    }

print(address_book["name"])
print(address_book["address"])

print(address_book.keys())
print(address_book.items())
print(address_book.values())