class Items():
    last_sku_used = 0
    def __init__(self, name, price, taxable):
        self.sku = Items.last_sku_used + 1
        self.name = name
        self.price = price
        self.taxable = taxable

        Items.last_sku_used = self.sku

    def get_full_item(self):
        """return the full item, price etc"""
        full_product = str(self.sku) + "Item Name " + self.name + " $" + "%.2f" %(self.price) + self.taxable
        return full_product.title()

    def get_item_tax_amount(self):
        taxed_item = self.price * 0.1498
        return "%.2f" %taxed_item

    def get_item_total(self):
        item_total = self.price * 1.1498
        return "%.2f" %item_total




itm1 = Items('banana', 10.00, "t")


print(itm1.get_full_item() + str(itm1.get_item_tax_amount()))
print("Item Total $" + str(itm1.get_item_total()))