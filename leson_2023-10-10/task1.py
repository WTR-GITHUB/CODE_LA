id_dictionary = {"id":"saulius", "pasword":"123456" }

while True:
    user_input = input("Enter your id: ")
    while id_dictionary["id"]!=user_input:
        print(f"You entered {user_input } no sutch user namne")
    break


while id_dictionary["id"]==user_input and id_dictionary["pasword"]==user_pass:
     
     if id_dictionary["id"]==user_input:
         print(f"Hello {user_input}")
         
         user_pass = input(f"Please enter pasword: ")
         if id_dictionary["pasword"]==user_pass:
            print(f"Access granted {user_input}")
            break
         else:
             print(f"You entered {user_pass } bad pasword! ")
     else:
         