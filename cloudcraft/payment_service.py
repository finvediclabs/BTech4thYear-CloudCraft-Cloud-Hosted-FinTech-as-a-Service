# Payment Service (with intentional bug)
class PaymentService:
    def __init__(self):
        self.active = False

    def start(self):
        self.active = True
        print("Payment Service started.")

    def stop(self):
        # Intentional bug: missing deactivation
        print("Payment Service stopped.")  # BUG: Should set self.active = False
