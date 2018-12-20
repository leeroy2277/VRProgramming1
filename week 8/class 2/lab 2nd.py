import datetime

x = datetime.datetime.now()

class Item:

    last_sku_used = 0

    def __init__(self, name, price, taxable):

        self.date = (x.strftime("%Y-%m-%d %I:%M%p").lower())

        self.sku = Item.last_sku_used + 1
        self.name = name
        self.price = price
        self.taxable = taxable
        Item.last_sku_used = self.sku

    def get_item_base_price(self):

        return self.price

    def get_item_fed_tax_amount(self):

        return self.price * 0.05

    def get_item_prov_tax_amount(self):

        return self.price * 0.09975

    def get_item_total(self):

        return self.get_item_base_price() + self.get_item_fed_tax_amount() + self.get_item_prov_tax_amount()

    def print_item_line(self):

        print(self.name, end="")
        print(".....................", end="")
        print('${:0,.2f}'.format(self.get_item_total()), end="")
        print(" ", end="")

        if self.taxable == True:
            print("T")
        else:
            print()


itm1 = Item('banana',100.00, True)

itm1.print_item_line()



