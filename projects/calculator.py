class Calculator(object):
    def __init__(self):
        self.last_answer = 0.0

    def add(self, a, b):
        self.last_answer = a + b
        return self.last_answer

    def subtract(self, a, b):
        self.last_answer = a - b
        return self.last_answer

    def multiply(self, a, b):
        self.last_answer = a * b
        return self.last_answer

    def divide(self, a, b):
        # automatically raises ZeroDivisionError
        self.last_answer = a * 1.0 / b
        return self.last_answer

    def maximum(self, a, b):
        self.last_answer = a if a >= b else b
        return self.last_answer

    def minimum(self, a, b):
        self.last_answer = a if a <= b else b
        return self.last_answer
