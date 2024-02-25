class Purchase:
    count_id = 0

    def __init__(self, customer):
        Purchase.count_id += 1
        self.products = []
        self.customer = customer
        self.id = Purchase.count_id

    def __str__(self):
        return (f'CUSTOMER:'
                f'\t{self.customer.__str__()}'
                f'PURCHASED ITEMS:')

    def print_products(self):
        for product in self.products:
            print(product.__str__())
