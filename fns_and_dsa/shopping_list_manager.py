product = {
    "pizza": 8,
    "yam": 90,
    "salt": 8
}

try:
    name = input("what do you want to order: ")
    qnt = int(input("how many quantity do ypu want to order: "))
    
    if product[name] <= qnt:
        raise valuError(f"{name} is not enough")
    
except KeyError:
    print("sorry there was an error")
except ValueError as ve:
    print(ve)
else:
    print(f"you bought {qnt} {name}")
finally:
    print("thanks for petronizing with us see you soon")
        



