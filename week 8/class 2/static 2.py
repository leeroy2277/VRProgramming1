class Item():

    last_sku_used = 0

    def __init__(self, name, price, taxable):

        self.sku = Item.last_sku_used + 1
        self.name = name
        self.price = price
        self.taxable = taxable

        Item.last_sku_used = self.sku

a1 = Item("first item", 2.00, True)

a2 = Item("second item", 2.00, True)

Print(a1.sku)
Print(a1.sku)
