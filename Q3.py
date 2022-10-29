# Pawan Kumar
# ID: 2046222

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity*self.item_price)}')
        pass
    pass


if __name__ == '__main__':
    print("Item 1")
    print("Enter the item name:")
    name = input()
    print("Enter the item price:")
    price = float(input())
    print("Enter the item quantity:")
    qty = int(input())
    product1 = ItemToPurchase()
    product1.item_name=(name)
    product1.item_price=(price)
    product1.item_quantity=(qty)
    print()
    print("Item 2")
    print("Enter the item name:")
    name = input()
    print("Enter the item price:")
    price = float(input())
    print("Enter the item quantity:")
    qty = int(input())
    product2 = ItemToPurchase()
    product2.item_name=(name)
    product2.item_price=(price)
    product2.item_quantity=(qty)
    print()
    print("TOTAL COST")
    product1.print_item_cost()
    product2.print_item_cost()
    print()
    print(f"Total: ${int((product1.item_quantity*product1.item_price)+(product2.item_quantity*product2.item_price))}")
    pass
