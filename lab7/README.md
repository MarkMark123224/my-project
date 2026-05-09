# Лабораторна робота 7
## Опис
Програма перевіряє товари у супермаркеті та знаходить ті,
термін придатності яких завершується найближчим часом.

## Запуск програми
python app.py

## Запуск тестів
python -m unittest test_app.py

## Запуск doctest
python -m doctest app.py -v

## Встановлення залежностей
pip install -r requirements.txt

## Перевірка стилю коду
flake8 app.py test_app.py

## Налаштування Git Hook
Створіть файл:
.git/hooks/pre-commit

Вставте у нього:
#!/bin/sh
echo "Перевірка коду за допомогою flake8..."
flake8 app.py test_app.py
if [ $? -ne 0 ]; then
    echo "Помилка форматування. Коміт скасовано."
    exit 1
fi
echo "Перевірка пройшла успішно."
exit 0

Для Linux або Git Bash зробіть файл виконуваним:
chmod +x .git/hooks/pre-commit
