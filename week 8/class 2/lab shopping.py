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

        length = self.name

        print(str (length).title() + ' ', end="")

        number_of_period = 30 - len(length)

        for y in range(number_of_period):

            print('.', end='')

        if self.taxable == True:
            print(' ${:0,.2f}'.format(self.get_item_total()), end="")

            print(" ", end="")

            print("T")

        else:
            print(' ${:0,.2f}'.format(self.get_item_base_price()), end="")

            print(" ", end="")



'''
while True:
    message = input("enter sku: ")
else:
    message2 = input("enter product name: ")
else:
    
    print(message)

    if message == "no":
        break



'''


itm1 = Item('banana',100.00, True)
itm2 = Item('thong',200.00, True)
itm3 = Item('milk', 1.00, False)


itm1.print_item_line()
itm2.print_item_line()
itm3.print_item_line()