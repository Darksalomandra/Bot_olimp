# TelegramBot Olimp

Телеграм бот позволяет получать информацию по школьным олимпиадам. 

## Установка 
Склонировать репозиторий:
```bash
git clone git@github.com:Darksalomandra/Bot_olomp.git
```

Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv source env/bin/activate # (Mac OS, Linux) или 
python -m venv venv && . venv/Scripts/activate # (Win10)
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
- Переименуйте файл .env.example на .env
- Поменяйте BOT_TOKEN

Запустить проект:
```bash
python app.py
```

## Запуск проекта в Docker

Установить Docker и Docker Compose
```bash
pip install docker
pip install docker-compose
```

Склонировать репозиторий:
```bash
git clone git@github.com:Darksalomandra/Bot_olomp.git
```

- Переименуйте файл .env.example на .env
- Поменяйте BOT_TOKEN

Запустить сборку контейнера Docker:
```bash
docker-compose up -d -bild
```

## Разработчик проекта

Автор: Abashin Mark 

E-mail: mabashin05@gmail.com

telegram: https://t.me/Darksalomandra