class CoreController:
    def __init__(self):
        self.customer_list = []
        self.product_list = []
        self.purchase_list = []

    def add_customer_to_list(self, new_customer):
        if new_customer is None:
            return
        self.customer_list.append(new_customer)
        for customer in self.customer_list:
            print(customer)

    def add_product_to_list(self, new_product):
        if new_product is None:
            return
        self.product_list.append(new_product)
        for product in self.product_list:
            print(product)

    def add_purchase_to_list(self, new_purchase):
        if new_purchase is None:
            return
        self.purchase_list.append(new_purchase)
        for purchase in self.purchase_list:
            print(purchase)

    def search_customer_by_nit(self, nit):
        for customer in self.customer_list:
            if customer.get_nit() == nit:
                return customer
        return None

    def search_product_by_code(self, product_code):
        for product in self.product_list:
            if product.code_product == product_code:
                return product
        return None
