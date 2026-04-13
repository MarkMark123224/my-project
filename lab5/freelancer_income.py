def calculate_hours_payment(hours, rate):
    """
    >>> calculate_hours_payment(10, 5)
    50
    >>> calculate_hours_payment(0, 10)
    0
    """
    if hours < 0 or rate < 0:
        raise ValueError("...")
    return hours * rate


def subtract_platform_fee(total_payment, fee_percent):
    """
    >>> subtract_platform_fee(100, 10)
    90.0
    >>> subtract_platform_fee(200, 0)
    200.0
    """
    if fee_percent < 0 or fee_percent > 100:
        raise ValueError("...")
    fee = total_payment * fee_percent / 100
    return total_payment - fee


def analyze_income(hours, rate, fee_percent):
    """
    >>> analyze_income(10, 5, 10)
    {'gross_income': 50, 'net_income': 45.0}
    """
    gross = calculate_hours_payment(hours, rate)
    net = subtract_platform_fee(gross, fee_percent)
    return {
        "gross_income": gross,
        "net_income": net
    }


def main():
    hours = int(input("Введіть години роботи: "))
    rate = float(input("Введіть ставку за годину: "))
    fee = float(input("Введіть комісію (у %): "))

    result = analyze_income(hours, rate, fee)

    print("Заробіток до комісії:", result["gross_income"])
    print("Чистий заробіток:", result["net_income"])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
