my_list_a = [1, 2, 3, 4, 5]
my_list_b = [10, 20, 30, 40, 50]

sum = 0
for item in my_list_a:
    sum += item
print("List suma: ",sum)

sum = 1
for item in my_list_a:
    sum *= item
print("List sandauga: ",sum)

print("Max sarase: ",max(my_list_a))
print("Min sarase: ",min(my_list_b))

txt = ""
for item in my_list_b:
    txt += f"{str(item)} "  
print(txt)

for item in my_list_b:
    my_list_a.append(item)
print(my_list_a)