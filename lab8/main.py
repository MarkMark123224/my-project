import os
import sentry_sdk


def init_sentry():
    sentry_sdk.init(
        dsn=os.getenv("https://53f2ec25bcafdd780a9c481e610dc1f2@o4511287037657088.ingest.de.sentry.io/4511361339949136"),
        send_default_pii=True,
    )


def analyze_http_codes(data):
    if not data.strip():
        raise ValueError("Порожній ввід")

    parts = data.split()

    for p in parts:
        if not p.isdigit():
            raise ValueError(f"Некоректне значення: {p}")

    return len(parts)


def main():
    init_sentry()

    try:
        print("Введіть HTTP коди через пробіл:")
        user_input = input()

        result = analyze_http_codes(user_input)
        print("Кількість кодів:", result)

    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise


if __name__ == "__main__":
    main()
