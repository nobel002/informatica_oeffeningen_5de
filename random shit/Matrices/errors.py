class DimentionMismatch(Exception):
    def __init__(self, dimention_a, dimention_b, message="The two dimentions do not match"):
        self.dimention_a = dimention_a
        self.dimention_b = dimention_b
        self.message = message
        super().__init__(self.message)
