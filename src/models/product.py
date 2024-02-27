class Product:
    code_basic_structure = 'PR00'
    count_product = 0

    def __init__(self, name, description, unit_price):
        Product.count_product += 1
        self.code_product = Product.code_basic_structure + str(Product.count_product)
        self.name = name
        self.description = description
        self.unit_price = unit_price

    def __str__(self):
        return (f'\t    Code Product: {self.code_product}\n'
                f'\t    Name Product: {self.name}\n'
                f'\t    Description: {self.description}\n'
                f'\t    Unit Price: {self.unit_price}')

    def get_code(self):
        return self.code_product

    def get_unit_price(self):
        return self.unit_price
