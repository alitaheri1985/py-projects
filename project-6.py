user_age = int(input("How old are you? "))
user_name = input("What is your name? ")

new_list = [[user_name, user_age]]
add_to_list = input("Do you want to add another name and age? (yes/no): ")
while add_to_list.lower() == "yes":
    user_age = int(input("How old are you? "))
    if type(user_age) != int:
        print("Please enter a valid age.")
        continue
    user_name = input("What is your name? ")
    if type(user_name) != str:
        print("Please enter a valid name.")
        continue
    new_list.append([user_name, user_age])
    add_to_list = input("Do you want to add another name and age? (yes/no): ")
    while add_to_list.lower() != "yes" and add_to_list.lower() != "no":
        if add_to_list.lower() == "no":
            break
        else:
            print("Please enter a valid response.")
        add_to_list = input("Do you want to add another name and age? (yes/no): ")
    #add_to_list = input("Do you want to add another name and age? (yes/no): ")
        
name_list =[x[0] for x in new_list]
age_list =[x[1] for x in new_list]
delatils_list = [f"{x[0]} is {x[1]}" for x in new_list]

print("=============================================================")
for x in delatils_list:
    print(x)