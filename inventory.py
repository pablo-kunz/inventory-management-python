# Module responsible for inventory logic: load, search, update and report

def name_exists(inventory, name):
    """Checks if a name already exists in the inventory (case and space insensitive)."""
    clean_name = name.strip().lower()
    for item in inventory:
        if item["tool"].strip().lower() == clean_name:
            return True
    return False


def load_tools(inventory):
    """Initial tool load. Only runs if the inventory is empty."""
    if len(inventory) > 0:
        print("Tools are already loaded. Use option 5 to add new products.")
        return inventory

    while True:
        try:
            quantity = int(input("How many tools do you want to load? "))
            if quantity <= 0:
                raise ValueError("The quantity must be an integer greater than zero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    loaded = 0
    while loaded < quantity:
        try:
            name = input(f"\nTool {loaded + 1} — Enter name: ")
            if name.strip() == "":
                raise ValueError("Name cannot be empty.")
            if name_exists(inventory, name):
                raise ValueError(f"A tool named '{name.strip()}' already exists.")

            stock = int(input(f"Enter initial stock for '{name.strip()}': "))
            if stock < 0:
                raise ValueError("Initial stock cannot be negative.")

            inventory.append({"tool": name.strip(), "quantity": stock})
            loaded += 1
            print(f"✔ '{name.strip()}' added with stock {stock}.")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    print(f"\nLoad complete. {quantity} tool(s) registered.")
    return inventory


def show_inventory(inventory):
    """Displays all tools and their current stock."""
    if len(inventory) == 0:
        print("No tools loaded in the inventory.")
        return

    print("\n========== INVENTORY ==========")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['tool']} — Stock: {item['quantity']}")
    print("================================")


def check_stock(inventory):
    """Searches for a tool by name and shows its stock."""
    if len(inventory) == 0:
        print("No tools loaded in the inventory.")
        return

    name = input("Enter the tool name to check: ")
    clean_name = name.strip().lower()

    for item in inventory:
        if item["tool"].strip().lower() == clean_name:
            print(f"'{item['tool']}' — Available stock: {item['quantity']} unit(s).")
            return

    print(f"Tool '{name.strip()}' was not found in the inventory.")


def out_of_stock_report(inventory):
    """Lists the tools with stock equal to zero."""
    if len(inventory) == 0:
        print("No tools loaded in the inventory.")
        return

    out_of_stock = []
    for item in inventory:
        if item["quantity"] == 0:
            out_of_stock.append(item["tool"])

    if len(out_of_stock) == 0:
        print("No products are out of stock.")
    else:
        print("\n========== OUT-OF-STOCK PRODUCTS ==========")
        for name in out_of_stock:
            print(f"  - {name}")
        print("=============================================")


def add_product(inventory):
    """Adds a single new tool to the inventory."""
    try:
        name = input("Enter the name of the new tool: ")
        if name.strip() == "":
            raise ValueError("Name cannot be empty.")
        if name_exists(inventory, name):
            raise ValueError(f"A tool named '{name.strip()}' already exists.")

        stock = int(input(f"Enter initial stock for '{name.strip()}': "))
        if stock < 0:
            raise ValueError("Initial stock cannot be negative.")

        inventory.append({"tool": name.strip(), "quantity": stock})
        print(f"✔ '{name.strip()}' added successfully with stock {stock}.")

    except ValueError as e:
        print(f"Error: {e}. Product was not added.")

    return inventory


def update_stock(inventory):
    """Allows registering a sale or a restock of merchandise."""
    if len(inventory) == 0:
        print("No tools loaded in the inventory.")
        return

    name = input("Enter the tool name: ")
    clean_name = name.strip().lower()

    index = -1
    for i, item in enumerate(inventory):
        if item["tool"].strip().lower() == clean_name:
            index = i
            break

    if index == -1:
        print(f"Tool '{name.strip()}' was not found in the inventory.")
        return

    print(f"\nTool: {inventory[index]['tool']} — Current stock: {inventory[index]['quantity']}")
    print("Operation type:")
    print("  1. Sale (decrease stock)")
    print("  2. Restock (increase stock)")

    try:
        operation_type = int(input("Select an option (1 or 2): "))
        if operation_type not in (1, 2):
            raise ValueError("Invalid option. Must enter 1 or 2.")

        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            raise ValueError("The quantity must be an integer greater than zero.")

        if operation_type == 1:
            if inventory[index]["quantity"] - quantity < 0:
                raise ValueError(
                    f"Insufficient stock. Available: {inventory[index]['quantity']} unit(s)."
                )
            inventory[index]["quantity"] -= quantity
            print(f"✔ Sale registered. Updated stock: {inventory[index]['quantity']} unit(s).")
        else:
            inventory[index]["quantity"] += quantity
            print(f"✔ Restock registered. Updated stock: {inventory[index]['quantity']} unit(s).")

    except ValueError as e:
        print(f"Error: {e}")
