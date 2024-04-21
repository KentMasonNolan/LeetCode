for num in range(51):

    output = ""

    if num == 0:
        continue

    if num % 3 == 0:
        output += "fizz"

    if num % 5 == 0:
        output += "buzz"

    if len(output) >0:
        print(num, ":", output)
