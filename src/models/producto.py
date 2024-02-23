class Product:
    def __init__(self, code_product, name, description, unit_price):
        self.code_product = code_product
        self.name = name
        self.description = description
        self.unit_price = unit_price

    def __str__(self):
        return (f'Code Product: {self.code_product}, Name Product: {self.name}, Description: {self.description}, Unit '
                f'Price: {self.unit_price}')


