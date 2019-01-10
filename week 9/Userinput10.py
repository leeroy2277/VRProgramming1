from ItemClass10 import Item
from OrderClass10 import Order
import datetime

#my order statement/input

order = Order()

while True:


     item_sku = input("Enter the item sku?:")

     item_name = input("Enter the name of the item?:")

     item_price = input("Enter the the price of the item?:")

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