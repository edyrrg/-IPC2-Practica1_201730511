class Purchase:
    def __init__(self, customer, id_purchase, invoice):
        self.products = list
        self.customer = customer
        self.id = id_purchase
        self.invoice = invoice

    def __str__(self):
        return (f'CUSTOMER:'
                f'\t{self.customer.__str__()}'
                f'PURCHASED ITEMS:')