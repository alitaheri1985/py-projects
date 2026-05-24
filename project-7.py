menu = {
        
    "name": "hamburger",
    "price" : 30000,
    "couint": 5,
    "meal" : 90,
    "potato": True,
    "recommendation": [
        {
            "name":"hotdog",
            "price": 325200,
            "count": 7,
            "meal": 60,
            "potato": True
        },
        {
            "name": "salad",
            "price": 5411100,
            "count": 2,
            "meal": False,
            "potatos": False

        }

    ] 
        
}

# print(menu["recommendation"])

for meal in menu["recommendation"]:
    print(meal["name"])
