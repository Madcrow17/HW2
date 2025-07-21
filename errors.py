class MyIndexError(IndexError):
    def __init__(self, index, message=None):
        if message is None:
            message = f"Индекс {index} выходит за пределы допустимого диапазона"
        super().__init__(message)
        self.index = index


class InvalidItemError(TypeError):
    def __init__(self, received_type):
        super().__init__(f"Ожидался объект типа Item или его наследник, а получен {received_type}")
