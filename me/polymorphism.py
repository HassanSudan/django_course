# Polymophism means let use single interface to work  with different data type or classes methods

# Example Payment 
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must be implement this method.")
    
class CreditCard(Payment):
    def process_payment(self, amount):
        return f"processing Credit Card payment of ${amount}"

class DebitCard(Payment):
    def process_payment(self, amount):
        return f"processing Debi Card payment of ${amount}"
    
class PayPal(Payment):
    def process_payment(self, amount):
        return f"processing PayPal payment of ${amount}"
    
    def _make_payment(Payment_method, amount):
        print(Payment_method.process_payment(amount))

if __name__ == "__main__":
    credit = CreditCard()
    debit = DebitCard()
    paypay = PayPal()


    make_payment(credit,100)
    make_payment(credit, 50)
    make_payment(PayPal, 200)




    