print ("                       comprehension of dictionaries                       ")
print("")
print("---------------------------Key Value Pair * 2----------------------------------")

dic1 = {
    "name": "ali",
    "age": 25,
    "city": "tehran"
}

double_items = {value * 2 for value in dic1.values()}


print(double_items)
print("")
print("-----------------------Create a Dictionary and identify 'odd' and 'even' number---------------------------------")
print("")
simple_num = {num: ("even" if num%2 == 0 else "odd") for num in range(11)}
print(simple_num)

