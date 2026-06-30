# Hardware Store Inventory Management System
# Main file: menu and program flow

from inventory import (
    load_tools,
    show_inventory,
    check_stock,
    out_of_stock_report,
    add_product,
    update_stock
)


def show_menu():
    print("\n========== MAIN MENU ==========")
    print("1. Initial tool stock load")
    print("2. Display inventory")
    print("3. Check stock")
    print("4. Out-of-stock report")
    print("5. Add new product")
    print("6. Update stock (Sale / Restock)")
    print("7. Exit")
    print("================================")


def main():
    inventory = []
    option = 0

    while option != 7:
        show_menu()
        try:
            option = int(input("Select an option: "))
            if option == 1:
                inventory = load_tools(inventory)
            elif option == 2:
                show_inventory(inventory)
            elif option == 3:
                check_stock(inventory)
            elif option == 4:
                out_of_stock_report(inventory)
            elif option == 5:
                inventory = add_product(inventory)
            elif option == 6:
                update_stock(inventory)
            elif option == 7:
                print("Exiting the system. Goodbye!")
            else:
                raise ValueError("The option must be between 1 and 7.")
        except ValueError:
            print("Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
