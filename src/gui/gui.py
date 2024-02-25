from src.controllers.core_controller import CoreController
from src.controllers.handler_input_user import handler_input_option as my_input_option
from src.controllers.handler_input_user import handler_response_user as my_input_response
from src.controllers.handler_input_user import handler_number_response_user as my_input_response_number
from src.controllers.handler_input_user import handler_yorn_response_user as my_input_response_yorn
from src.models.customer import Customer

from src.models.product import Product


class GUI(object):
    def __init__(self, ui_data):
        self.ui_data = ui_data
        self.core_controller = CoreController()

    def init_core_ui(self):
        print(self.ui_data['hello'])
        while True:
            print(self.ui_data['principal_menu'])
            response_user = my_input_option(1, 6)
            if response_user == 1:
                new_product = self.add_new_product()
                self.core_controller.add_product_to_list(new_product)
            elif response_user == 2:
                new_customer = self.add_new_customer()
                self.core_controller.add_customer_to_list(new_customer)
            elif response_user == 3:
                print(self.search_product())
            elif response_user == 4:
                self.init_shopping_menu()
            elif response_user == 5:
                self.show_student_data()
            elif response_user == 6:
                print("Option 6 -- exit")
                break

    def show_student_data(self):
        print(f'\n{self.ui_data['student_data']}\n')

    def add_new_product(self):
        print(self.ui_data['new_product'])
        while True:
            print('\t    Enter code product:')
            product_code = my_input_response(3)
            print('\t    Enter name product:')
            product_name = my_input_response(4)
            print('\t    Enter description product:')
            product_description = my_input_response(8)
            print('\t    Enter unit price:')
            product_unit_price = my_input_response_number()
            print(f'\n\t    Code Product - {product_code}'
                  f'\n\t    Name Product - {product_name}'
                  f'\n\t    Unit Price - {product_unit_price}'
                  f'\n\t    Description Product - {product_description}'
                  f'\n\t    This product data is correct?'
                  f'\n{self.ui_data['question_yorn']}')
            is_correct = my_input_response_yorn()
            if is_correct:
                return Product(product_code, product_name, product_description, product_unit_price)
            elif is_correct is False:
                print(f'\n\t    Re-enter the product data again or return to the main menu?\n{self.ui_data['question_yorn']}')
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
                  f'\n\t    This customer data is correct?'
                  f'\n{self.ui_data['question_yorn']}')
            is_correct = my_input_response_yorn()
            if is_correct:
                return Customer(customer_name, customer_email, customer_nit)
            elif is_correct is False:
                print(f'\n\t    Re-enter the customer data again or return to the main menu?\n{self.ui_data['Q_yorn']}')
                is_correct = my_input_response_yorn()
                if is_correct is False:
                    return None

    def add_new_purchase(self):
        print(self.ui_data['new_purchase'])
        while True:
            customer_target = self.search_customer()
            if customer_target is not None:
                print(f'\n\t    The customer selection\n\t    {customer_target.__str__()}')
            else:
                print('\n\t    Customer not found - back to main menu')
                break




    def search_customer(self):
        while True:
            print('\t    Enter NIT Customer to search for...')
            customer_nit = my_input_response_number()
            res = self.core_controller.search_customer_by_nit(customer_nit)
            if res is not None:
                return res
            print('\t    There is no customer with this NIT')
            print('\t    Continue searching?...')
            print(f'\t    {self.ui_data['question_yorn']}')
            is_response_continue = my_input_response_yorn()
            if is_response_continue is False:
                print('\t    Customer not found...')
                print(f'{self.ui_data['back_to_principal_menu']}')
                return None

    def search_product(self):
        while True:
            print('\t    Enter code product to search for add to purchase...')
            product_code = my_input_response(3)
            res = self.core_controller.search_product_by_code(product_code)
            if res is not None:
                return res
            print('\t    There is no product with this Product Code...')
            print(self.ui_data['question_yorn'])
            responser_yorn = my_input_response_yorn()
            if responser_yorn is True:
                continue
            else:
                break


    def init_shopping_menu(self):
        while True:
            print(self.ui_data["shopping_menu"])
            response_user = my_input_option(1, 2)
            if response_user == 1:
                self.search_product()
            elif response_user == 2:
                print(self.ui_data["finishing_purchase"])
                break
            else:
                print('Invalid option, occurs an error on my_input_option')

