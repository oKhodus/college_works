import pytest

def type_check(*expected_types):
    """
    Decorator which check types of function arguments
    """
    def decorator(func):
        """Actual decorator function that wraps target function

        Args:
            func (function): original function whicj will be decorated
        """
        def wrapper(*args):
            """Checks types of arguments which go to the function 

            Raises:
                TypeError: raises if type of argument doesn't match to expected type

            Returns:
                Result of original function if types match
            """
            for i in range(len(args)):
                if type(args[i]) != expected_types[i]:
                    raise TypeError(f"Argument {i + 1} must be of type {expected_types[i]}, got {type(args[i])}")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(x, y):
    """Adds two integers to each other

    Args:
        x (int): first int
        y (int): second int

    Returns:
        int: summary of x and y
    """
    return x + y

print(add(5, 5))


@type_check(str, int)
def repeat_word(word, times):
    """Repeats a word by specified number of times

    Args:
        word (str): word which will be repeated
        times (int): number of times to repeat the word

    Returns:
        str: repeated word
    """
    return word * times

print(repeat_word("ok", 10))


def test_TypeError():
    """
    Tests TypeErrors:
    - if to "add()" write str instead of int
    - if to "repeat_word()" write str instead of int
    """
    with pytest.raises(TypeError):
        add(5, 'add')

    with pytest.raises(TypeError):
        repeat_word("hello", "bye")