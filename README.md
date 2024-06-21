# Тестовое задание для компании RLT

## Описание задачи
Стек: Python3, Asyncio, MongoDB, любая асинхронная библиотека для телеграм бота

Вашей задачей в рамках этого тестового задания будет написание алгоритма агрегации 
статистических данных о зарплатах сотрудников компании по временным промежуткам.

После разработки алгоритма агрегации, вам необходимо создать телеграм бота,
который будет принимать от пользователей текстовые сообщения содержащие JSON
с входными данными и отдавать агрегированные данные в ответ.

### Usage


```bash
git clone git@github.com:AndreyKilanov/RLT_testovoe.git
```

```bash
cd infra/
```

```bash
docker-compose up -d --build
```

### Example .env
location `infra/`

```bash
BOT_TOKEN=TG_BOT_TOKEN
DB_NAME=sample_db
DB_COLLECTION_NAME=sample_collection
DB_ADMIN_NAME=root
DB_ADMIN_PASSWORD=root
```

### Setup
1. [x] Python 3.11
2. [x] Motor 3.4.0
3. [x] Aiogram 3.7.0
4. [x] MongoDB
5. [x] Docker