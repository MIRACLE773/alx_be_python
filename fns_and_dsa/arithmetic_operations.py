products = {
    "pizza": 5,
    "bread": 10
}

try:
    item = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    # ✅ Check if we have enough in stock
    if products[item] >= quantity:
        print(f"✅ You bought {quantity} {item}(s).")
        products[item] -= quantity  # Reduce the stock
    else:
        raise ValueError("❌ Not enough stock.")

except KeyError:
    print("❌ Product not found in our store.")
except ValueError as ve:
    print(ve)
except Exception as e:
    print("❌ Something else went wrong:", e)
else:
    print("🎉 Your order was processed successfully.")
finally:
    print("✅ Thank you for visiting our store.")
