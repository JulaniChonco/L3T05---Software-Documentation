def divide_nums(num1, num2):
    """
    Divide two numbers.

    :param num1: The numerator.
    :type num1: float or int
    :param num2: The denominator (non-zero).
    :type num2: float or int
    :return: The result of the division.
    :rtype: float or int
    :raises ZeroDivisionError: If the denominator is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return num1 / num2
