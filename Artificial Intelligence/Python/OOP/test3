# You need to create the 8 classes complete with their attributes and methods.

class Customer:

    def __init__(self, name, loyal_customer):
        self.name = name
        self.loyal = loyal_customer


class Order:

    def __init__(self, customer):
        self.customer = customer
        self.list = []
        self.cost = []
        self.discount = []

    def add_to_order(self, item):
        self.list.append(item)
        self.cost.append(item.price)
        self.discount.append(item.discount)

    def summarise_order(self):
        print("Customer: {:s}". format(self.customer.name))
        print("Total items order: {:d}". format(len(self.list)))
        for item in self.list:
            item.summarise_order()
        if not self.customer.loyal:
            print("Total cost: £{:.2f}". format(sum(self.cost)))
        else:
            print("Today you saved £{:.2f}". format(sum(self.discount)))
            print("Today cost: £{:.2f}". format((sum(self.cost) - sum(self.discount))))


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0.0


class Drink(Item):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
        self.discount = 0.1


class Tea(Drink):
    def __init__(self, name, price, size, flavour):
        super().__init__(name, price, size)
        self.flavour = flavour

    def summarise_order(self):
        print("{} £{:.2f}, {}, {}". format(self.name, self.price, self.size, self.flavour))


class MineralWater(Drink):
    def __init__(self, name, price, size, order):
        super().__init__(name, price, size)
        self.order = order

    def summarise_order(self):
        print("{} £{:.2f}, {}". format(self.name, self.price, self.size))
        if not self.order:
            print("Still water")


class Sandwich(Item):
    def __init__(self, name, price, colour, type):
        super().__init__(name, price)
        self.colour = colour
        self.type = type
        self.discount = 0.2

    def summarise_order(self):
        print("{} £{:.2f}, {}, {}". format(self.name, self.price, self.colour, self.type))


class Cake(Item):
    def __init__(self, name, price, size, flavour, order):
        super().__init__(name, price)
        self.size = size
        self.flavour = flavour
        self.order = order

    def summarise_order(self):
        print("{} £{:.2f}, {}, {}". format(self.name, self.price, self.size, self.flavour))
        if self.name == "Chocolate dream":
            print("Warning: contains nuts!")



def main():
    # Create two customers...
    cust1 = Customer('Harry Palmer', False)
    cust2 = Customer('Bill Preston', True)  # A loyal regular customer

    # Order some items...
    order1 = Order(cust1)
    order1.add_to_order(Tea('Black tea', 2.00, 'large', 'Earl Gray'))
    order1.add_to_order(Sandwich('Club special', 4.50, 'brown', 'chicken'))

    order2 = Order(cust2)
    order2.add_to_order(MineralWater('Evian', 1.50, 'small', False))
    order2.add_to_order(Sandwich('Simple sandwich', 1.50, 'white', 'cheese'))
    order2.add_to_order(Cake('Chocolate dream', 2.30, 'medium', 'chocolate', True))

    # Summarise our orders...
    order1.summarise_order()
    print()
    order2.summarise_order()
    print()


if __name__ == "__main__":
    main()
