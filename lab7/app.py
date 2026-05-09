from datetime import datetime


def find_expiring_products(products):
    """
    >>> products = [
    ...     {"name": "Молоко", "expiry": "2026-05-10"},
    ...     {"name": "Сир", "expiry": "2026-05-20"},
    ...     {"name": "Хліб", "expiry": "2026-05-09"}
    ... ]
    >>> find_expiring_products(products)
    ['Хліб', 'Молоко']
    """

    today = datetime.today()

    expiring = []

    for product in products:
        expiry_date = datetime.strptime(product["expiry"], "%Y-%m-%d")

        days_left = (expiry_date - today).days

        if days_left <= 7:
            expiring.append(product["name"])

    return sorted(expiring)


def main():
    products = [
        {"name": "Молоко", "expiry": "2026-05-10"},
        {"name": "Сир", "expiry": "2026-05-20"},
        {"name": "Хліб", "expiry": "2026-05-09"},
    ]

    result = find_expiring_products(products)

    print("Товари з терміном придатності, що скоро завершиться:")

    for product in result:
        print(product)


if __name__ == "__main__":
    main()
