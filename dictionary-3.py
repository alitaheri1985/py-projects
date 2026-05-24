print("                            Dictionary Methods                           ")
print("")
dic1 = {"name": "Alice","age": 30,"city": "New York","email": "alice@example.com"}

print("============================= Clear Dictionary ===================================")
print("dic1 is: ", dic1)
dic1.clear() # Clear the dictionary
print("----------------------------------------------------------------")
print("dic1 is: ", dic1)
print("")
print("============================= Copy & compare dictionaries ===================================")
print("")
dic1 = {"name": "Alice","age": 30,"city": "New York","email": "alice@example.com"}
dic2 = dic1.copy()  # Create a shallow copy of the dictionary
print("dic2 is: ", dic2)
print("----------------------------------------------------------------")
print("Original dictionary: ", dic1)
print("----------------------------------------------------------------")
print("Copied dictionary: ", dic2)
print("")
print("Are the dictionaries equal?", dic1 == dic2)  # Check if the original and copied dictionaries are equal
print("Are the dictionaries the same?", dic1 is dic2)  # Check if the original and copied dictionaries are the same
print("")

print("============================= generate default values by fromkeys ===================================")
print("")
keys = ["name", "age", "city" , "matin"]  # List of keys for the new dictionary
value = "null"         # Default value for all keys in the new dictionary
dic3 = dict.fromkeys(keys, value)  # Create a new dictionary with specified keys and a default value
print(dic3)     #result: {'name': 'null', 'age': 'null', 'city': 'null'}
print("")

print("============================= Get value by key with get() method ===================================")
print("")
# Get the value associated with a key in a dictionary using the get() method
# which returns 'None' if the key does not exist in the dictionary, instead of raising a 'KeyError'.
dic1 = {"name": "Alice","age": 30,"city": "New York","email": "alice@example.com"}
print("dic1 is: ", dic1)
print("")
print("--------------------print a not exist value by get method-----------------------------")
print("")
print(dic1.get("phone"))  # This will return 'None' since "phone" is not a key in the dictionary
print("")
print("--------------------print a not exist value by square brackets------------------------")
print("")
print(dic1[phone])  # This will raise a KeyError since "phone" is not a key in the dictionary
