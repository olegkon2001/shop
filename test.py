class Store:
    pay_rate = 0.85
    item_list = []

    def __init__(self, name=None, price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.item_list.append(self)

    def full_price(self):
        return self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity