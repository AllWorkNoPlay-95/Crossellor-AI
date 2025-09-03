def bucket_number(number, step=5) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")
    lower = (number // step) * step
    upper = lower + step
    return f"{lower}-{upper}"
