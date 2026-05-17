import time
import getpass
password = ""
password1 = getpass.getpass("Enter your New password: ")
password2 = getpass.getpass("Confirm your New password: ")
while password1 != password2:
        
    print("it doesn't match. Please try again.")
    password1 = getpass.getpass("Enter your New password: ")
    password2 = getpass.getpass("Confirm your New password: ")
if password1 == password2:
    password = password1
    print("Your password has been set successfully.")
    print("")
    print("========================================================")
    print("")
    print("Type 'test' to test your password or 'exit' to quit.")
    if input() == "test":
        test_password = ""
        while test_password != password:
            test_password = getpass.getpass("Enter your password to test: ")
            if test_password == password:
                print("Password is correct!")
                print("Thank you for using our program. Goodbye!")
                time.sleep(5)
            else:
                print("Incorrect password. Please try again.")
    else:
        wait = input("Are you sure you want to exit? (yes/no): ")
        if wait == "yes":
            print("Thank you for using our program. Goodbye!")
            time.sleep(5)
        else:
            test_password = ""
            while test_password != password:
                test_password = getpass.getpass("Enter your password to test: ")
                if test_password == password:
                    print("Password is correct!")
                    print("Thank you for using our program. Goodbye!")
                    time.sleep(5)
                else:
                    print("Incorrect password. Please try again.")
        