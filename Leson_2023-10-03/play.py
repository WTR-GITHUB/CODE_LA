name = input("Write your name: ")
surname = input("Write your surname: ")
age = input("Enter your age: ")

my_name_list = []
my_surname_list = []
my_age_list = []

my_name_list.append(name)
my_surname_list.append(surname)
my_age_list.append(age)

print(my_name_list, my_surname_list, my_age_list)

my_dictionary = {"name": my_name_list, "surname": my_surname_list, "age": my_age_list} 
print(my_dictionary)

age_cap = 21

if age > age_cap:
    print(f"{name} {surname} your are welcome to our casino!")
else:
    print(f"{name} {surname} your are nor alowed to enter!")