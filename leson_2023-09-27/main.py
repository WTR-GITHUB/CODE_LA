import datetime

local_y = datetime.date.today().year

set_no1 = input('Koks pirmas skaicius? \n')
set_no2 = input('Koks antras skaicius? \n')
set_age = input('Koks tavo amzius? \n')
set_sentence = input('Ivesk sakini: \n')
set_letter = input('Ivesk raide: \n')

print(f"Skaiciu sudėtis: {int(set_no1)+int(set_no2)}")
print(f"Skaiciu atmintis: {int(set_no1)-int(set_no2)}")
print(f"Skaiciu daugyba: {int(set_no1)*int(set_no2)}")
print(f"Skaiciu dalyba: {int(set_no1)/int(set_no2)}")
print(f"Skaiciu islyginamasis coeficientas: {int(set_no1)//int(set_no2)}")
print(f"Skaiciu dalybos liekana: {int(set_no1)%int(set_no2)}")
print(f"Skaicio kelimas antru skaiciumi: {int(set_no1)**int(set_no2)}")

print(f"Tu gimei: {local_y-int(set_age)}")

print(f"Atvirkscias sakinys: {set_sentence[::-1]}")

print(f"Tekstas ismetant kas antra simboli: {set_sentence[::2]}")

print(f"Tavo ivestame sakinyje jei buvo balse a pakeiteme: {set_sentence.replace('a',set_letter)}")

my_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","Д8¢d€76н19klмиØq0Я$тuvШ%Ч5")
print(set_sentence.upper().translate(my_table))