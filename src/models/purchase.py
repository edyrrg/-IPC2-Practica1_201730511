from src.models.invoice import Invoice


class Purchase:
    count_id = 0

    def __init__(self, customer):
        Purchase.count_id += 1
        self.products_list = []
        self.customer = customer
        self.id = Purchase.count_id
        self.invoice = None

    def __str__(self):
        print(f'\t  PURCHASE ID - {self.id}\n'
              f'\t  CUSTOMER:\n'
              f'{self.customer.__str__()}\n'
              f'\t  PURCHASED ITEMS:')
        self.print_products()
        print(f'\t  Invoice Description\n'
              f'{self.invoice.__str__()}')

    def print_my_report(self):
        print(f'\t  ___ REPORT PURCHASE -- ID {self.id} ___\n'
              f'\t  CUSTOMER:\n'
              f'{self.customer.__str__()}\n'
              f'\t  PURCHASED ITEMS:')
        self.print_products()
        print(f'\t  Invoice Description\n'
              f'{self.invoice.__str__()}')

    def print_products(self):
        for product in self.products_list:
            print('\t    ----------------')
            print(product.__str__())
        print('\t    ----------------')

    def get_products__str__(self):
        for product in self.products_list:
            return product.__str__()

    def add_product_to_purchase_list(self, new_product):
        if new_product is not None:
            self.products_list.append(new_product)
            print(f'\t    Add new product to list...')
            self.print_products()

    def generate_invoice(self):
        if len(self.products_list) == 0:
            return
        tmp = 0
        for product in self.products_list:
            tmp += product.get_unit_price()
        self.invoice = Invoice(tmp)

    def products_list_is_empty(self):
        if len(self.products_list) == 0:
            return True
