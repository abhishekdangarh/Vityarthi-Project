def add_stock(items):

    print("\n----- ADD STOCK -----")

    item_id = input("Enter Item ID: ")
    quantity = int(input("Enter quantity to add: "))

    for item in items:

        if item["id"] == item_id:

            item["quantity"] += quantity

            print("\nStock added successfully!")
            print("New Stock:", item["quantity"])

            return

    print("Item not found.")