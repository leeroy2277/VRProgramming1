import datetime

class Item:

    line_len =30

    def __init__(self, sku, name, price: float, taxable):

        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable


    def is_taxable(self):
        if (self.taxable == True):
            return "T"
        else:
            return ""


    def get_sku(self):

        return self.sku

    def get_name(self):

        return self.name

    def get_item_base_price(self):

        return self.price

    def get_item_fed_tax_amount(self):

        if self.taxable:

            return self.price * 0.05

        else:

            return 0

    def get_item_prov_tax_amount(self):

        if self.taxable:

            return self.price * 0.09975

        else:

            return 0

    def get_item_total(self):

        return self.get_item_base_price() + self.get_item_fed_tax_amount() + self.get_item_prov_tax_amount()

    def print_item(self,width):

        price = self.get_item_base_price()

        dots = "."*(width-len(self.name))

        price = "${:0.2f}".format(price)

        print(self.name,dots,price,self.is_taxable())
