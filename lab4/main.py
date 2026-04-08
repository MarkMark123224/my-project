items = {}


def addItem(name, price, quantity):
    if name in items:
        items[name]["quantity"] += quantity
    else:
        items[name] = {
            "price": price,
            "quantity": quantity
        }

    total_price = price * quantity
    print(
        f"Додано: {name} | К-сть: {quantity} | "
        f"Ціна: {price} | Всього: {total_price}"
    )


def removeItem(name, quantity):
    if name not in items:
        print("Товар не знайдено")
        return

    if items[name]["quantity"] < quantity:
        print("Недостатньо товару")
        return

    price = items[name]["price"]
    total_price = price * quantity

    items[name]["quantity"] -= quantity

    if items[name]["quantity"] == 0:
        del items[name]

    print(
        f"Видалено: {name} | К-сть: {quantity} | "
        f"Ціна: {price} | Всього: {total_price}"
    )


def calculateStockValue():
    total = 0
    print("\nТовари на складі:")

    for name, item in items.items():
        item_total = item["price"] * item["quantity"]
        print(f"{name}: {item['quantity']} * {item['price']} = {item_total}")
        total += item_total

    return total


# Тест
addItem("Ноутбук", 30000, 2)
addItem("Мишка", 500, 5)
addItem("Клавіатура", 1500, 3)

removeItem("Мишка", 2)

print("\nЗагальна вартість:", calculateStockValue())
