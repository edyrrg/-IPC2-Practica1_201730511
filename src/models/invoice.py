class Invoice:
    count_invoices = 0
    TAX_RATE = 0.12

    def __init__(self, subtotal):
        Invoice.count_invoices += 1
        self.invoice_id = Invoice.count_invoices
        self.subtotal = subtotal
        self.tax = Invoice.TAX_RATE * self.subtotal
        self.total = self.subtotal + self.tax

    def get_subtotal(self):
        return self.subtotal

    def get_tax(self):
        return self.tax

    def get_total(self):
        return self.total

    def __str__(self):
        return (f'\t   Invoice ID: {self.invoice_id}\n'
                f'\t   Subtotal: {self.subtotal}\n'
                f'\t   Tax: {self.tax}\n'
                f'\t   Total: {self.total}\n')
