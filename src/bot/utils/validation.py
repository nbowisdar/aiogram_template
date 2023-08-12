from typing import Any, Callable, Type


def check_mobile_number(value: any) -> bool | str:
    if value[0] != "+":
        return False
    elif len(value) < 9 or len(value) > 14:
        return False

    return value


def simple_check_digit(value: any, t: Type[int] | Type[float]) -> int | float:
    try:
        if t == int:
            return int(value)
        elif t == float:
            return float(value)
        raise Exception("Wrong type")
    except ValueError:
        return False


def check_digit_or_function(
        value: any, t: int | float, func: Callable, *args, **kwargs
) -> Any:
    try:
        if t == int:
            return int(value)
        elif t == float:
            return float(value)
        raise Exception("Wrong type")
    except ValueError:
        return func(value, *args, **kwargs)


async def async_check_digit_or_function(
        value: any, t: int | float, func: Callable, *args, **kwargs
) -> Any:
    try:
        if t == int:
            return int(value)
        elif t == float:
            return float(value)
        raise Exception("Wrong type")
    except ValueError:
        return func(value, *args, **kwargs)
