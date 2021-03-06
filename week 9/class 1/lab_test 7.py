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

    def is_taxable(self):

        return self.taxable

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

    def print_item_line(self):

        length = self.name

        print(str (length).title() + ' ', end="")

        number_of_period = 30 - len(length)

        for y in range(number_of_period):

            print('.', end='')

        print(' ${:0,.2f}'.format(self.get_item_total()), end="")

        if self.taxable == True:

            print(" T")


class Order:

    def __init__(self):

        self.items = []

        self.date = (x.strftime("%Y-%m-%d %I:%M%p").lower())

    def add_item(self, item: Item):

        self.items.append(item)


    def get_item_count(self):

        return len(self.items)

    def get_total_gst(self):

        total_gst = 0

        for item in self.items:

            if item.is_taxable():

                total_gst = total_gst + item.get_item_fed_tax_amount()

        return total_gst

    def get_total_pst(self):

        total_pst = 0

        for item in self.items:

            if item.is_taxable():

                total_pst = total_pst + item.get_item_prov_tax_amount()

        return (total_pst)

    def get_total_price(self):

        total_price = 0

        for item in self.items:

            total_price = total_price + item.get_item_base_price()

        return (total_price)

    def print_items(self):

        for item in self.items:
            item.print_item()


    def generate_reciept(self):

        print("{} {:>34} {:>14} ".format('Item','Price','Taxable'))
        print("_____________________")
        self.print_items()
        print("________")
        print()
'''
    def generate_receipt(self,width):
        dash = '-' * 55
        print("Order Number : {:>10}".format(self.order_number))
        #print("Item Number : {:>10}".format(self.get_item_count()))
        dtime = '{:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())
        print("Order Date: {:>40}".format(dtime))
        print()
        print("{} {:>34} {:>14} ".format('Item','Price','Taxable'))
        print(dash)
        self.print_items(width)
        print(dash)
        print()

'''







# TEST
'''
it1 = Item("banana", 100, True)
it2 = Item("apple", 100, False)

o = Order()

o.add_item(it1)
o.add_item(it2)


print ("Total GST on the order is " + str(o.get_total_gst()))
print ("Total PST on the order is " + str(o.get_total_pst()))
print ("Total price on the order is " + str(o.get_total_price()))
'''

# TEST

order = Order()

while True:


    # item_sku = input("What is the item sku? >")

     item_name = input("What is the the name of the item? >")

     item_price = input("What is the the price of the item? >")

     item_taxable = input("Is the item taxable(y/n)? >")
     taxable = False
     if item_taxable == 'y':
         taxable = True



     new_item = Item( item_name, item_price, taxable)
     order.add_item(new_item)

     Next = input("Enter Next y for yes n for no ")
     if Next == "n":
         break



Order.generate_reciept()


itm1 = Item(item_name, int(item_price), item_taxable )

itm1.print_item_line()

itm1 = Item(item_name, int(item_price), item_taxable )

itm1.print_item_line()

#order.print_order()

'''
itm1 = Item(new_item)
itm2 = Item('thong',200.00, True)
itm3 = Item('milk', 1.00, False)


itm1.print_item_line()
itm2.print_item_line()
itm3.print_item_line()
'''