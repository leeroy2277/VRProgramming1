import datetime

x = datetime.datetime.now()
class Item:

    line_len =30

    def __init__(self, sku, name, price: float, taxable):

        self.date = (x.strftime("%Y-%m-%d %I:%M%p").lower())
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

        print("{} {} {} {} ".format(self.name,dots,price,self.is_taxable()))





class Order:

    last_serial_used = 0

    def __init__(self):

        self.items = []

        self.__order_number = Order.last_serial_used + 1

        Order.last_serial_used = self.__order_number

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

    def print_items(self, width):

        for item in self.items:
            item.print_item(width)



    def generate_receipt(self, width):

        print()

        print("Thank you, come again!")

        print()

        order_no ="{:06d}".format(self.__order_number)

        print("{} {:>24}".format("Order Number :", order_no))

        dtime = '{:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())

        print("Order Date: {:>40}".format(dtime))

        print()

        print("{} {:>42} ".format('Item','Price'))

        self.print_items(width)

        print()



        #print taxes



        sub_total_price = "${:0.2f}".format(float(self.get_total_price()))

        print("{} {:<5} ".format('Subtotal ', sub_total_price))


        total_gst = "${:0.2f}".format(float(self.get_total_gst()))

        total_pst = "${:0.2f}".format(float(self.get_total_pst()))

        print("{} {:<5} ".format('Tax GST ', total_gst))

        print("{} {:<5} ".format('Tax QST ', total_pst))


        total=self.get_total_price() + self.get_total_gst() + self.get_total_pst()

        total_price = "${:0.2f}".format(float(total))

        print("{} {:<5} ".format('TOTAL ',  total_price))


order = Order()

while True:


     item_sku = input("What is the item sku?:")

     item_name = input("What is the the name of the item?:")

     item_price = input("What is the the price of the item?:")

     item_taxable = input("Is the item taxable?(y/n):")

     taxable = False
     if item_taxable == 'y':
         taxable = True

     new_item = Item(item_sku, item_name, float(item_price), taxable)
     order.add_item(new_item)

     Next = input("Would you like to enter another item?(y/n): ")

     if Next == "n":

         break


order.generate_receipt(40)