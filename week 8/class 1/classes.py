class item:
    tax_increase = 0
    def __init__(self, sku, name, price, taxable: True):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable
        









    __isbn = 0

    def __init__(self, input_isbn):
        self.__isbn = input_isbn

    def set_isbn(self, set_to_isbn):
        self.__isbn = set_to_isbn

    def get_isbn(self):
        return self.__isbn

new_book = Book(123456)

new_book.set_isbn(23456)

print(new_book.get_isbn())