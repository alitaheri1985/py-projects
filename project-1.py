# This program converts data volume from GB to MB. It prompts the user to enter a data volume in GB,
# converts it to MB by multiplying by 1024 (since 1 GB = 1024 MB), rounds the result to 2 decimal places, and displays it to the user.

# print a message to the user asking for data volume in GB
print("please enter your data volume in GB: ")

# get the data volume from the user and convert it to a float
data_volume = float(input())

# convert the data volume from GB to MB by multiplying it by 1024
result  = data_volume * 1024

# round the result to 2 decimal places
result = round(result,2)

# print the result to the user
print (f"your data volume in MB is: {result} MB")

