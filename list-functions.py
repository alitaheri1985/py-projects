# List functions

list1= ["Asus", "HP", "Acer", "Dell", "HP", "Lenovo"]

# print(list1)
# #======================================================Append, Insert, Extend========================================================
# # to append an object to the end of the list
# # if we use of an object that is a list, it will be added as a single element to the end of the list like a nested list
# list1.append("Apple")
# list1.append(["Cisco", "Microsoft"])

# #to insert an object at a specified index
# list1.insert (2, "Samsung")

# #to extend a list by appending all the items from another list to the end of the list
# list1.extend(["Sony", "Toshiba"])

# print(list1)

# #======================================================Clear, Remove, Pop========================================================

# #to clear all the elements from a list, we can use the clear() method. This will remove all the items from the list and leave it empty.
# list1.clear()

# #to removethe first occurrence of a specified value from the list, we can use the remove() method. If the value is not found in the list, it will raise a ValueError.
# list1.remove("Apple")

# #to remove an item at a specified index, we can use the pop() method. If no index is specified, it will remove and return the last item in the list.
# list1.pop(3)


# print(list1)

# #======================================================Index, Count, Sort, Reverse========================================================

# #to find the index of the first occurrence of a specified value in the list, we can use the index() method.
# #If the value is not found in the list, it will raise a ValueError.
# index = list1.index("Dell")
# print(index)

# #to find a specified value in the specified range of the list, we can use the index() method with the start and end parameters.
# # This will return the index of the first occurrence of the value within the specified range.
# # its useful when we want to search for a value index when we have multiple occurrences of the same value in the list.
# index = list1.index("HP", 2, 5)
# print(index)

# #to count the number of occurrences of a specified value in the list, we can use the count() method.
# #its good to use this method to check if an item is present in the list or not or there are multiple occurrences of the same item in the list.
# count = list1.count("HP")
# print(count)

# #to sort the elements of the list in ascending order, we can use the sort() method.
# list1.sort()
# print(list1)

# #to reverse the order of the elements in the list, we can use the reverse() method.
# list1.reverse()
# print(list1)

# #======================================================Copy, slice, Join, Len, Max, Min========================================================

# #to create a shallow copy of the list, we can use the copy() method. This will create a new list with the same elements as the original list.
# list2 = list1.copy()
# print(list2)

# #to create a new list that contains a portion of the original list, we can use slicing. This will create a new list that contains the elements from the specified start index to the specified end index (not including the end index).
# list3 = list1[1:4]
# print(list3)

# #to create a new list that containe a portion of original list, we can use slicing with a step value. This will create a new list that contains the elements from the specified start index to the specified end index (not including the end index) with the specified step value.
# list4 = list1[0:5:2]
# print(list4)

# #to reverse the order of the elements in the list, we can use slicing with a step of -1. This will create a new list that contains the elements of the original list in reverse order.
# list4 = list1[::-1]
# print(list4)

# #to join two lists, we can use the + operator or the extend() method. The + operator will create a new list that contains all the elements from both lists, while the extend() method will add the elements of one list to the end of another list.
# list2 = " - ".join(list1)
# print(list2)

# #to get the length of the list, we can use the len() function. This will return the number of elements in the list.
# length = len(list1)
# print(length)

# #to let the maximum value in the list, we can use the max() function. This will return the largest element in the list.
# max_value = max(list1)
# print(max_value)

# #to let the minimum value in the list, we can use the min() function. This will return the smallest element in the list.
# min_value = min(list1)
# print(min_value)

#======================================================List Comprehension========================================================

# List comprehension is a concise way to create lists. It allows us to create a new list by applying an expression to each element of an existing list.
# squares = [x * 2 for x in list1]
# print(squares)

# new_list = [x for x in list1 if "A" in x]
# print(new_list)

# new_list = [x.upper() if "A" in x else x.lower() for x in list1] 
# print(new_list)                                         

#======================================================Nested List Comprehension========================================================

# Nested list comprehension is a way to create a new list by applying an expression to each element of an existing nested list.
# A nested list is a list that contains other lists as its elements.

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = [x * 2 for sublist in nested_list for x in sublist]
# print(new_list)

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