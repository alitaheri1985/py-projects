# This program converts data volume from MB to TB and checks for valid input. It prompts the user to enter a data volume in MB,
# checks if the input is valid (not negative or zero), and if valid, converts it to TB by dividing by 1024 twice
# (since 1 TB = 1024 GB and 1 GB = 1024 MB). The result is rounded to 2 decimal places and displayed to the user.

# get the data volume from the user and convert it to a float
data_volume = float(input("please enter your data volume in MB: "))

# check if the data volume is negative or zero and print an error message if it is
if data_volume < 0:
    print ("data volume cannot be negative. Please enter a valid number.")
elif data_volume == 0:
    print ("data volume cannot be zero. Please enter a valid number.")
else:
    result  = data_volume / 1024 / 1024
    result = round(result,2)
    print (f"your data volume is: {result} TB")

