# Geekshop

Учебный проект онлайн-магазина на Django2.2.17

## Установка зависимостей:

pip install -r requirements.txt

## Формирование БД продуктов:

./manage.py loaddata mainapp/fixtures/categories.json ./manage.py loaddata mainapp/fixtures/products.json

## Запуск сервера (порт 8000):

./manage.py runserver

