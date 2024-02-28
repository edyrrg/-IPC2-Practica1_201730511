from src.controllers.core_controller import CoreController
from src.controllers.handler_input_user import handler_input_option as my_input_option
from src.controllers.handler_input_user import handler_response_user as my_input_response
from src.controllers.handler_input_user import handler_number_response_user as my_input_response_number
from src.controllers.handler_input_user import handler_yorn_response_user as my_input_response_yorn
from src.controllers.handler_input_user import handler_continue_response_user as my_input_response_continue
from src.models.customer import Customer

from src.models.product import Product
from src.models.purchase import Purchase


class GUI(object):
    def __init__(self, ui_data):
        self.ui_data = ui_data
        self.core_controller = CoreController()

    def init_core_ui(self):
        print(f'{self.ui_data['hello']}')
        while True:
            print(f'{self.ui_data['principal_menu']}')
            response_user = my_input_option(1, 6)
            if response_user == 1:
                new_product = self.add_new_product()
                if new_product is not None:
                    self.core_controller.add_product_to_list(new_product)
            elif response_user == 2:
                new_customer = self.add_new_customer()
                if new_customer is not None:
                    self.core_controller.add_customer_to_list(new_customer)
            elif response_user == 3:
                new_purchase = self.add_new_purchase()
                if new_purchase is not None:
                    new_purchase.generate_invoice()
                    self.core_controller.add_purchase_to_list(new_purchase)
            elif response_user == 4:
                self.core_controller.print_report_purchase()
            elif response_user == 5:
                self.show_student_data()
            elif response_user == 6:
                print(f'\n{self.ui_data['good_bye']}')
                break

    def show_student_data(self):
        print(f'\n{self.ui_data['student_data']}\n')

    def add_new_product(self):
        print(self.ui_data['new_product'])
        while True:
            # print('\t    Enter code product:')
            # product_code = my_input_response(3)
            print('\t    Enter name product:')
            product_name = my_input_response(4)
            print('\t    Enter description product:')
            product_description = my_input_response(8)
            print('\t    Enter unit price:')
            product_unit_price = my_input_response_number()
            # f'\n\t    Code Product - {product_code}'
            print(f'\n\t    Name Product: {product_name}'
                  f'\n\t    Description product: {product_description}'
                  f'\n\t    Unit Price: {product_unit_price}'
                  f'\n\n\t    This product data is correct?'
                  f'\n{self.ui_data['question_yorn']}')
            is_correct = my_input_response_yorn()
            if is_correct:
                return Product(product_name, product_description, product_unit_price)
            elif is_correct is False:
                print(f'\n{self.ui_data['re_enter_product_data']}'
                      f'\n{self.ui_data['question_yorn']}')
                is_correct = my_input_response_yorn()
                if is_correct is False:
                    return None

    def add_new_customer(self):
        print(self.ui_data['new_customer'])
        while True:
            print('\t    Enter name:')
            customer_name = my_input_response(3)
            print('\t    Enter email:')
            customer_email = my_input_response(10)
            print('\t    Enter nit')
            customer_nit = my_input_response_number()
            print(f'\n\t    Name Customer: {customer_name}'
                  f'\n\t    Email Customer: {customer_email}'
                  f'\n\t    NIT Customer: {customer_nit}'
                  f'\n\n\t    This customer data is correct?'
                  f'\n{self.ui_data['question_yorn']}')
            is_correct = my_input_response_yorn()
            if is_correct:
                return Customer(customer_name, customer_email, customer_nit)
            elif is_correct is False:
                print(f'\n{self.ui_data['re_enter_customer_data']}'
                      f'\n{self.ui_data['question_yorn']}')
                is_correct = my_input_response_yorn()
                if is_correct is False:
                    return None

    def add_new_purchase(self):
        print(self.ui_data['new_purchase'])
        if self.core_controller.products_data_list_is_empty() is True:
            print(f'{self.ui_data['products_list_is_empty']}')
            return None

        if self.core_controller.customer_data_list_is_empty() is True:
            print(f'{self.ui_data['customer_list_is_empty']}')
            return None

        while True:
            customer_pick = self.search_customer()
            if customer_pick is not None:
                print(f'\n{self.ui_data['customer_pick']}\n'
                      f'{customer_pick.__str__()}')
                current_purchase = Purchase(customer_pick)
                self.init_shopping_menu(current_purchase)
                current_purchase.generate_invoice()
                print('\t    -----------------')
                current_purchase.__str__()
                print('\t    -----------------')
                print(f'\t    This purchase data is correct?'
                      f'\n{self.ui_data['question_yorn']}')
                is_correct = my_input_response_yorn()
                if is_correct:
                    return current_purchase
                elif is_correct is False:
                    print(f'\n{self.ui_data['re_enter_purchase_data']}'
                          f'\n{self.ui_data['question_yorn']}')
                    is_correct = my_input_response_yorn()
                    if is_correct is False:
                        return None

    def search_customer(self):
        while True:
            print(self.ui_data['nit_customer_to_search'])
            customer_nit = my_input_response_number()
            res = self.core_controller.search_customer_by_nit(customer_nit)
            if res is not None:
                return res
            print(self.ui_data['not_customer_found'])
            print(self.ui_data['continue_searching'])
            print(f'\t    {self.ui_data['question_continue']}')
            is_response_continue = my_input_response_continue()
            if is_response_continue is False:
                print(f'{self.ui_data['back_to_principal_menu']}')
                return None

    def search_product(self):
        while True:
            print(self.ui_data['code_product_to_search'])
            product_code = my_input_response(3)
            res = self.core_controller.search_product_by_code(product_code)
            if res is not None:
                return res
            print(self.ui_data['not_product_found'])
            print(self.ui_data['continue_searching'])
            print(self.ui_data['question_continue'])
            response_yorn = my_input_response_continue()
            if response_yorn is True:
                continue
            else:
                break

    def init_shopping_menu(self, new_purchase):
        while True:
            print(self.ui_data["shopping_menu"])
            response_user = my_input_option(1, 2)
            if response_user == 1:
                new_product = self.search_product()
                new_purchase.add_product_to_purchase_list(new_product)
            elif response_user == 2:
                if new_purchase.products_list_is_empty() is not True:
                    print(self.ui_data["finishing_purchase"])
                    return
                else:
                    print(self.ui_data['empty_products_list'])
            else:
                print('Invalid option, occurs an error on my_input_option')
