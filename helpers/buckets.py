def bucket_number(number, step) -> str:
    """
    Convert a number into a bucket range string.
    Args:
        number: Number to convert (can be string, float, or int)
        step: Size of the bucket range
    Returns:
        String representing the bucket range (e.g., "0-5")
    Raises:
        ValueError: If number is negative or cannot be converted to float
    """
    if isinstance(number, str):
        try:
            number = float(number.replace(',', '.'))
        except ValueError:
            raise ValueError("String value must be a valid number")

    if number < 0:
        raise ValueError("Number must be non-negative")

    lower = (int(number) // step) * step
    upper = lower + step
    return f"{lower}-{upper}"
