# for num in range(1, 11):
#     for num2 in(1,):
#         result = num * num2
#         print(result * "*")

for num in range(1,11):
    if num % 2 != 0:
        for star in range(1,5):
            print("*" * star)
    else:
        for star in range(4,0,-1):
            print("*" * star)



