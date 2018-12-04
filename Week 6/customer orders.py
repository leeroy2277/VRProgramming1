def create_order(customer, *skus):
    print("The customer name is : " + customer)

    for sku in skus:
        print(sku)

customer_name="Customer1"

create_order(customer_name, 1234567, 2345678, 3456789, 8888888)
