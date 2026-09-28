def sell_item(items):

    print("\n----- SELL ITEM -----")

    item_id = input("Enter Item ID: ")
    quantity = int(input("Enter quantity to sell: "))

    for item in items:

        if item["id"] == item_id:

            if quantity <= item["quantity"]:

                item["quantity"] -= quantity

                print("\nItem sold successfully!")
                print("Remaining Stock:", item["quantity"])

            else:

                print("Not enough stock available.")

            return

    print("Item not found.")