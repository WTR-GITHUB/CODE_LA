values = range(10)
my_list = []
my_tuple_list = []

for i in values:
    no_ent = int(input(f"Enter {i+1} no: "))
    if no_ent < 50:
        my_list.append(no_ent)
    else:
        my_tuple_list.append(no_ent)

print(my_list)
print(tuple(my_tuple_list))

print(max(my_list)-min(my_list))
print(sum(my_tuple_list))