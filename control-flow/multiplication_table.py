number = int(input("enter a number too see a multiplication table: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")