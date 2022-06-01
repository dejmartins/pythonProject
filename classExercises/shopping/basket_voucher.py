class BasketVoucher:
    def __init__(self):
        self.items = []
        self.voucher = 0

    def cart_can_take_only(self, items):
        self.voucher = items

    def add(self, item):
        if self.number_of_items() == self.voucher:
            self.items = self.items[1:]
            self.items.append(item)
        else:
            self.items.append(item)

    def number_of_items(self):
        return len(self.items)

    def replace(self, this_item, another_item):
        position = self.items.index(this_item)
        self.items.remove(this_item)
        self.items.insert(position, another_item)
