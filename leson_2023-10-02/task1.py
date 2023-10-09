# Program takes 3 random numbers as user input. 
# Update lsit and tuple data structures with those values and print it.

# nr_first = input("Enter first no: ")
# nr_second = input("Enter second no: ")
# nr_third = input("Enter third no: ")

# my_list = []
# my_tuple = (nr_first, nr_second, nr_third)

# my_list.append(nr_first)
# my_list.append(nr_second)
# my_list.append(nr_third)

# print(my_list)
# print(my_tuple)

# Create a program, which takes 10 random numbers as user inputs.
# The program should produce list of input values what are less than 50 and tuple
# of all other values.
# After input is done, program should return the the mathematical difference between
# the highest and lowest number, and sum of primary numbers
# from tuple.
# 1. 
# 2. Nustatyti is ju max ir min
# 3. ats = max - min
# 4. sum tuple list 


nr_1 = int(input("Enter 1 no: "))
nr_2 = int(input("Enter 2 no: "))
nr_3 = int(input("Enter 3 no: "))
nr_4 = int(input("Enter 4 no: "))
nr_5 = int(input("Enter 5 no: "))
nr_6 = int(input("Enter 6 no: "))
nr_7 = int(input("Enter 7 no: "))
nr_8 = int(input("Enter 8 no: "))
nr_9 = int(input("Enter 9 no: "))
nr_10 = int(input("Enter 10 no: "))

my_list = []
my_tuple_list = []

if nr_1 < 50:
    my_list.append(nr_1)
else:
    my_tuple_list.append(nr_1)
if nr_2 < 50:
    my_list.append(nr_2)
else:
    my_tuple_list.append(nr_2)
if nr_3 < 50:
    my_list.append(nr_3)
else:
    my_tuple_list.append(nr_3)
if nr_4 < 50:
    my_list.append(nr_4)
else:
    my_tuple_list.append(nr_4)
if nr_5 < 50:
    my_list.append(nr_5)
else:
    my_tuple_list.append(nr_5)
if nr_6 < 50:
    my_list.append(nr_6)
else:
    my_tuple_list.append(nr_6)
if nr_7 < 50:
    my_list.append(nr_7)
else:
    my_tuple_list.append(nr_7)
if nr_8 < 50:
    my_list.append(nr_8)
else:
    my_tuple_list.append(nr_8)
if nr_9 < 50:
    my_list.append(nr_9)
else:
    my_tuple_list.append(nr_9)
if nr_10 < 50:
    my_list.append(nr_10)
else:
    my_tuple_list.append(nr_10)

print(my_list)
print(tuple(my_tuple_list))

print(max(my_list)-min(my_list))
