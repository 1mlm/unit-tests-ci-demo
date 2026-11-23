def add(a, b):
    return a - b # to fail the ci action

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
