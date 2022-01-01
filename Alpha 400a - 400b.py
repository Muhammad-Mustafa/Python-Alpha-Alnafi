
'''              بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ            '''


'''Alpha 400a - 400b'''

"""Loopes"""

for numbers in range(5):
    print(numbers)
print("-----------------------------------")
for numbers in [1,2,3,4,5]:
    print(numbers)
    

print("-----------------------------------")

temp_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4
    }

for key in temp_dict:
    print("the key in this dict is = ",key,' the value of that key is = ',temp_dict[key])
print("-----------------------------------")
a_dict = {
    1: "one",
    10:"two",
    3:"three"      
    }

keys = a_dict.keys()
print("keys == ",keys)

sorted_keys = sorted(keys)
print("sorted keys ==", sorted_keys)
for key in sorted_keys:
    print(key)
    
print("-----------------------------------")
for number in range(50):
    if number % 2 == 0:
        print(number)
        
print("-----------------------------------")
for number in range(50):
    if number % 2 == 1:
        print(number)
        
print("-----------------------------------")
#i = 2
#while i < 10:
#    print(0)

print("-----------------------------------")

i = 0
while i < 10:
    print(i)
    i += 1

print("-----------------------------------")

j = 0
while j < 10:
    print(j)
    if j ==5:
        break
    j += 1

print("-----------------------------------")

my_list = [1,2,3,4,5,6,7,8,9,10]

for val in my_list:
    if val ==9:
        print("Item no ", val, " is found in the database")
    else:
        print("we are at item no ", val, " the item 9 is not found yet :(")