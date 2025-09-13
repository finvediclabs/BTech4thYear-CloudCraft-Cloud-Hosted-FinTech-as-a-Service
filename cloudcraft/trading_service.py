# Trading Service (with intentional bug)
class TradingService:
    def __init__(self):
        self.active = False

    def start(self):
        # Intentional bug: should set self.active = True
        self.active = False  # BUG: Should be True
        print("Trading Service started.")

    def stop(self):
        self.active = False
        print("Trading Service stopped.")
