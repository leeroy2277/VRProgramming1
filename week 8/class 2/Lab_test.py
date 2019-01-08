import datetime

x = datetime.datetime.now()


class Item:
    #last_sku_used = 0



    def __init__(self, Item_Name, Price, taxable):

        self.date = (x.strftime("%Y-%m-%d %I:%M%p").lower())

        self.name = Item_Name

        self.price = Price

        self.taxable = taxable



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

        print(str(length).title() + ' ', end="")

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


i = 0

while True:

    i += 1

    itemlist = []

    Sku = int(input("enter sku: "))
    Item_Name = input("enter Item: ")
    Price = int(input("enter Price: "))
    tax = input("Is item Taxable y for yes n for no ")
    taxable = False
    if tax == 'y':
        taxable = True


    Next = input("Enter Next y for yes n for no ")
    if Next == "n":
        break

    itemlist.append(i,Sku,Item_Name,Price,taxable)


    print()



print(itemlist)























