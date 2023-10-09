name = input("Write your name: ")
surname = input("Write your surname: ")
age = int(input("Enter your age: "))

vip_list = ["Saulius", "Mindaugas", "Valdas"]

age_cap = 21

if age > age_cap:
    if name in vip_list:
        print(f"{name} {surname} your are welcome to our casino!")
    else:
        print(f"Your are welcome to our casino!")
else:
     print(f"Your are nor alowed to enter!")


