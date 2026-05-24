print("============================= Check is exists key in the dictionary ===================================")
print("")
dic1 = {"name": "Alice", "age": 30, "city": "New York"}
isExist = "email" in dic1
print(isExist)

print("============================= Check key exists in the dictionary by 'if'condition ===================================")
print("")
dic2 = {"name": "Bob", "age": 25, "city": "Los Angeles", "email": "bob@example.com"}
if "email" in dic2:
    print(dic2["email"])
else:
    print("Email does not exist in the dictionary.")

print("============================= Check is exists value in the dictionary ===================================")
print("")
dic1 = {"name": "Alice", "age": 30, "city": "New York"}
isExist = "email" in dic1
print(isExist)