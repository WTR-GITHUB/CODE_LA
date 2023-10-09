name = input("Write your name: ")
surname = input("Write your surname: ")
age = input("Enter your age: ")

prop_eye_color = input("Enter your eye color: ")
prop_hair_color = input("Enter your hair color: ")
prop_skin_color = input("Enter your skin color: ")
prop_height = input("Enter your height: ")
prop_weight = input("Enter your weight: ")

properties = {"eye_color":prop_eye_color,
              "hair_color":prop_hair_color,
              "skin_color":prop_skin_color,
              "height":prop_height,  
              "weight":prop_weight}

my_dictionary = {"name": name, "surname": surname, "age": age, "properties":properties}

print(my_dictionary)