class Customer:
    def __init__(self, name, email, nit):
        self.name = name
        self.email = email
        self.nit = nit

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, NIT: {self.nit}'

    def get_nit(self):
        return self.nit
