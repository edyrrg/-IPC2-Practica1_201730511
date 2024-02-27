class Customer:
    def __init__(self, name, email, nit):
        self.name = name
        self.email = email
        self.nit = nit

    def __str__(self):
        return (f'\t    Name: {self.name}\n'
                f'\t    Email: {self.email}\n'
                f'\t    NIT: {self.nit}')

    def get_nit(self):
        return self.nit
