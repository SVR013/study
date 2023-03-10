from functools import wraps


def validate_args(func):
    '''Функция-декоратор'''
    @wraps(func)
    def examination(*args) -> int | str | None:
        if len(args) != 2:
            return 'Мало аргументов'\
                if len(args) < 2\
                else 'Много аргументов'
        if len(args) == 2:
            return func(*args)\
                if isinstance(args[0], int) and isinstance(args[1], int)\
                else 'Неправильный тип аргументов'
        return None

    return examination


@validate_args
def add_numbers(arg1: int, arg2: int) -> int:
    """Возвращает сумму x и y"""
    return arg1 + arg2


if __name__ == "__main__":
    print(add_numbers(4, 5))
