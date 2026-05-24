#============================ Basic Concepts of Dictionary ===================================
print("")

#= Dictionary Example =#
dic1 = {"product: ": "Watch", "count: ": 25, "price: ": 100}
print("Dic1:", dic1)

print("")
print("============================ Employee Dictionary as list ===================================")
print("")

#= Employee Details =#
employees = [dict(name= "Ali", age= 39, city="Tehran"), dict(name= "Reza", age= 25, city="Isfahan")]
print("employees:", employees)
print

print("")
print("============================ Employee by List index ===================================")
print("")

#= Employee List =#
print (employees[0]["name"], employees[0]["age"], employees[0]["city"])     # Print the details of the first employee
print (employees[1]["name"], employees[1]["age"], employees[1]["city"])     # Print the details of the second employee

print("")
print("============================ Dictionary Items (for loop) ===================================")
print("")

#= Dic1 Item (for loop) =#
for item in dic1.items():
    print(item)  # Print each item in the dictionary

print("")
print("============================ Dictionary Keys (for loop) ===================================")
print("")

#= Dic1 Key (for loop) =#
for key in dic1.keys():
    print(key)  # Print each key in the dictionary

print("")
print("============================ Dictionary Values (for loop) ===================================")
print("")

#= Dic1 Value (for loop) =#
for value in dic1.values():
    print(value)  # Print each value in the dictionary

print("")
print("============================ Dictionary key-value pair (for loop) ===================================")    
print("")

#= Dic1 Key Value (for loop) =#
for key, value in dic1.items():
    print(key, value)  # Print each key-value pair in the dictionary

print("")
print("============================ Employee Detail in 2 ways (for loop) ===================================")
print("")

#= Employee List (for loop) =#
for employee in employees:
    print(employee)  # Print each employee in the list
    print(employee["name"], employee["age"], employee["city"])  # Print the details of each employee


