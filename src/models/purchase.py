class Purchase:
    count_id = 0

    def __init__(self, customer):
        Purchase.count_id += 1
        self.products_list = []
        self.customer = customer
        self.id = Purchase.count_id
        self.subtotal_purchase = 0
        self.taxes = 0
        self.total_purchase = 0

    def __str__(self):
        return (f"PURCHASE ID {self.id}"
                f'CUSTOMER:'
                f'\t{self.customer.__str__()}'
                f'PURCHASED ITEMS:'
                f'\t{self.print_products()}')

    def print_products(self):
        for product in self.products_list:
            print(product.__str__())

    def add_product_to_purchase_list(self, new_product):
        if new_product is not None:
            self.products_list.append(new_product)
            print(f'\t    add new product to list {self.products_list}')
            self.print_products()

    def calculate_subtotal_and_taxes(self):
        for product in self.products_list:
            self.subtotal_purchase += product.unit_price
        self.taxes = self.subtotal_purchase * 0.12
        self.total_purchase = self.subtotal_purchase + self.taxes

    def get_subtotal(self):
        return self.subtotal_purchase

    def get_taxes(self):
        return self.taxes

    def get_total_purchase(self):
        return self.total_purchase
