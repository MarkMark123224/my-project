# Lab2_Python

## Створення віртуального оточення
python -m venv venv

## Активація
venv\Scripts\activate

## Встановлення бібліотек
pip install requests
pip install pip-audit

## Перевірка версії бібліотеки
pip show requests
pip show pip-audit

## Запуск програми
python main.py

## Збереження залежностей
pip freeze > requirements.txt

## Встановлення залежностей
pip install -r requirements.txt

## Перевірка вразливостей
pip-audit -r requirements.txt

## Оновлення пакету (за потреби)
pip install --upgrade pip

## .gitignore
venv/
__pycache__

