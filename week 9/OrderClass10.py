from ItemClass10 import Item
import datetime

class Order:

    last_serial_used = 0

    def __init__(self):

        self.items = []

        self.__order_number = Order.last_serial_used + 1

        Order.last_serial_used = self.__order_number

        self.date = (datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p").lower())


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

        return total_pst

    def get_total_price(self):

        total_price = 0

        for item in self.items:

            total_price = total_price + item.get_item_base_price()

        return total_price

    def print_items(self, width):

        for item in self.items:
            item.print_item(width)



    def generate_receipt(self, width):

        #Print a message after order submitted

        print()

        print("Thank you, come again!")

        #print order number and date/time

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

        print('Subtotal: ', sub_total_price)

        total_gst = "${:0.2f}".format(float(self.get_total_gst()))

        total_pst = "${:0.2f}".format(float(self.get_total_pst()))

        print('Tax GST: ', total_gst)

        print('Tax PST: ', total_pst)

        #print grand total


        total=self.get_total_price() + self.get_total_gst() + self.get_total_pst()

        total_price = "${:0.2f}".format(float(total))

        print('TOTAL: ',  total_price)


