from add_item import add_item
from available_items import available_items
from stock import add_stock
from sell_item import sell_item


# Store all shop items
items = []


while True:

    print("\n================================")
    print("      SHOP MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add New Item")
    print("2. Available Item List")
    print("3. Add Stock")
    print("4. Sell Item")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        add_item(items)

    elif choice == "2":

        available_items(items)

    elif choice == "3":

        add_stock(items)

    elif choice == "4":

        sell_item(items)

    elif choice == "5":

        print("\nThank you for using Shop Management System!")
        break

    else:

        print("\nInvalid choice!")