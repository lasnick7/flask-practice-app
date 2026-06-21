[![Maintainability](https://qlty.sh/gh/lasnick7/projects/flask-practice-app/maintainability.svg)](https://qlty.sh/gh/lasnick7/projects/flask-practice-app)

# Flask Quote Manager

Учебное веб-приложение на Flask, созданное в рамках практики по веб-разработке.

Проект позволяет просматривать, добавлять и удалять цитаты. Данные сохраняются в локальной SQLite-базе данных.

Деплой: https://flask-practice-app-qd0c.onrender.com/
## Стек

- Python
- Flask
- SQLite
- HTML
- CSS
- uv

## Возможности

- Просмотр главной страницы
- Просмотр списка цитат
- Добавление новой цитаты
- Удаление цитаты
- Страница "О проекте"
- Динамический маршрут приветствия пользователя

## Локальный запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/YOUR_USERNAME/flask-practice-app.git
cd flask-practice-app
```

2. Установить зависимости:

```bash
uv sync
```

3. Запустить приложение:

```bash
uv run python app.py
```

4. Открыть в браузере:

```
http://127.0.0.1:5000
```