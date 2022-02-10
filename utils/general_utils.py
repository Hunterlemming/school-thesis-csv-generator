

def int_to_string(num: int) -> str:
    return f"0{num}" if (num < 10) else f"{num}"


class CustomError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)