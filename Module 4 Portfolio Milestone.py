class ItemToPurchase:
    def __init__(self, name=None, price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def CreateItem(name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def main():
    print("Item 1")
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase(name, price, quantity)

    print("Item 2")
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase(name, price, quantity)

    print("TOTAL COST")
    print(f"{item1.name} {item1.quantity} @ ${int(item1.price):d} = ${int(item1.quantity * item1.price):d}")
    print(f"{item2.name} {item2.quantity} @ ${int(item2.price):d} = ${int(item2.quantity * item2.price):d}")
    print(f"Total: ${int(item1.price * item1.quantity + item2.price * item2.quantity):d}")

main()
