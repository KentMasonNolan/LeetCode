FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

for i in range(0, len(FLAVORS)):
    for j in range(i+1, len(FLAVORS)):
        print(str(FLAVORS[i])+ ", " + str(FLAVORS[j]))
