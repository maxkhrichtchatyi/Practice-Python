from functools import wraps


def make_paragraph(fn):
    """Defines the decorator."""

    # Define the inner function
    @wraps(
        fn
    )  # This makes the decorator transparent in terms of its name and docstring
    def decorator():
        return "<p>" + fn() + "</p>"

    return decorator


@make_paragraph
def say_hello() -> str:
    """Say hello function."""

    return "Hello"


# Check the result of decoration
print(say_hello())

# Check if the function name is still the name of the function being decorated
print(say_hello.__name__)

# Check if the function docstring is still the name of the function being decorated
print(say_hello.__doc__)
