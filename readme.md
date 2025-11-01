# Repeats Bot

Простой эхо-бот для Telegram с подсчётом пользователей, которого создал ChatGPT.

**Протестировать бота:** [https://t.me/repeats_bot](https://t.me/repeats_bot)

## Установка и запуск

1. Склонируй репозиторий:

```bash
git clone https://github.com/king-tri-ton/repeats.git
cd repeats
```

2. Создай файл `.env` на основе примера `.env.example`:

```bash
cp .env.example .env
```

3. Открой `.env` и вставь свои значения:

* `TOKEN` — токен, полученный у [@BotFather](https://t.me/botfather)
* `ADMIN` — ID администратора (можно получить через бота [@username_to_id_bot](https://t.me/username_to_id_bot))
* `DB_NAME` — имя базы данных (по умолчанию `repeats`)

4. Установи зависимости:

```bash
pip install -r requirements.txt
```

5. Запусти бота:

```bash
python bot.py
```

## Использование

* `/start` — зарегистрироваться и получить приветственное сообщение.
* `/stat` — показать статистику пользователям, для администратора выводится количество пользователей.

Любые другие сообщения бот будет повторять (эхо).

## Лицензия

Проект распространяется по лицензии [MIT](LICENSE).
