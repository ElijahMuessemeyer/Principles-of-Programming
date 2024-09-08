class ItemToPurchase:
    def __init__(self, name=None, price=0, quantity=0, description=""):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description


class ShoppingCart:
    def __init__(self, customer_name="Customer", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed")

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.price != 0:
                    cart_item.price = item.price
                elif item.quantity != 0:
                    cart_item.quantity = item.quantity
                elif item.description != "":
                    cart_item.description = item.description
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = 0
            for item in self.cart_items:
                cost = item.price * item.quantity
                print(f"{item.name} {item.quantity} @ ${item.price} = ${cost}")
                total_cost += cost
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")


def print_menu(cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    while True:
        try:
            choice = input("Choose an option: ")
            if choice == 'q':
                break
            elif choice == 'a':
                print("ADD ITEM TO CART")
                name = input("Enter the item name:\n")
                description = input("Enter the item description:\n")
                price = float(input("Enter the item price:\n"))
                quantity = int(input("Enter the item quantity:\n"))
                item = ItemToPurchase(name, price, quantity, description)
                cart.add_item(item)
            elif choice == 'r':
                print("REMOVE ITEM FROM CART")
                name = input("Enter name of item to remove:\n")
                cart.remove_item(name)
            elif choice == 'c':
                print("CHANGE ITEM QUANTITY")
                name = input("Enter the item name:\n")
                quantity = int(input("Enter the new quantity:\n"))
                item = ItemToPurchase(name, 0, quantity, "")
                cart.modify_item(item)
            elif choice == 'i':
                cart.print_descriptions()
            elif choice == 'o':
                cart.print_total()
            else:
                print("Invalid option. Please try again.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


main()