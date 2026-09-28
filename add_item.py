def add_item(items):

    print("\n----- ADD NEW ITEM -----")

    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    price = float(input("Enter Price: ₹"))
    quantity = int(input("Enter Quantity: "))

    # Grade according to price
    if price <= 1000:
        grade = "0"
    elif price <= 1200:
        grade = "A"
    elif price <= 1400:
        grade = "B"
    elif price <= 1600:
        grade = "C"
    elif price <= 1800:
        grade = "D"
    elif price <= 2000:
        grade = "E"
    else:
        grade = "F"

    item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "grade": grade
    }

    items.append(item)

    print("\nItem added successfully!")
    print("Grade:", grade)