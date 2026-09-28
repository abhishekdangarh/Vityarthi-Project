def available_items(items):

    print("\n----- AVAILABLE ITEMS -----")

    found = False

    for item in items:

        if item["quantity"] > 0:

            print("----------------------------")
            print("Item ID :", item["id"])
            print("Name    :", item["name"])
            print("Price   : ₹", item["price"])
            print("Stock   :", item["quantity"])
            print("Grade   :", item["grade"])

            found = True

    if found == False:
        print("No items available in stock.")