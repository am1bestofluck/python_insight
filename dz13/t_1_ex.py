class NegativeValueError(Exception):
    def __init__(self, value_name: str, err_val: int | float):
        self.err = err_val
        self.mask = value_name

    def __str__(self):
        return f"expected positive value on {self.mask}, got {self.err}"


if __name__ == '__main__':
    raise NegativeValueError("width", -100)
