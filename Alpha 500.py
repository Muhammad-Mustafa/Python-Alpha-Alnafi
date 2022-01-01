
'''              بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ            '''


'''Alpha 500'''

"""Comprehensions"""

x = [i for i in range(5)]
print(x)


print("-----------------------------------")


'''y = [i for i in line if "Some Term" in i]
print(y)'''

print("-----------------------------------")


a = [str(i) for i in range(5)]
print(a)

a = [int(i) for i in a]
print(a)

print("-----------------------------------")


my_String_list = ["  aasdsa   ", '     ssss'," sssss  "]
print(my_String_list) 

my_list =[s.strip() for s in my_String_list]        
print(my_list)  


print("-----------------------------------")


num_list = [[1,2,3],[4,5,6],[7,8,9]]
print(num_list)

single_list = [val for items in num_list for val in items]
print(single_list)

print("-----------------------------------")


my_dict = {
    i: str(i) for i in range(5)
    }
print(my_dict)

print("-----------------------------------")


dict_2 = {
    1: 'dog',
    2: 'cat',
    3: 'cow'
    }

print({value:key for key,value in dict_2.items()})


print("-----------------------------------")


country = 'Pakistan'
letter_list1 = []
for letter in country:
    letter_list1.append(letter)
print(letter_list1)

letter_list2 = [letter for letter in country]
print(letter_list2)
    