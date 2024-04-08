## Executing program

Клонирование:

```sh
$ git clone https://github.com/Cagey7/fitness_api.git
$ cd fitness_api
```

### Запуск с докером

```sh
$ docker compose -f development.yml up
```

Для запуска production поменяйте название файла .env.example на .env

```sh
$ docker compose -f production.yml up
```

### Запустить локально

1) Создать виртуальную среду

```sh
$ python -m venv venv
$ .\venv\Scripts\activate
```

2) Установить зависимости

```sh
(venv) $ pip install -r .\requirements\development.txt
```

ВАЖНО! Введите ваши настройки базы данных в файл technoshop/settings/development.py

3) Запустите миграцию

```sh
(venv) $ python manage.py migrate --settings=fitness_api.settings.development
```

4) Если хотите заполнить базу данных данными можете запустить

```sh
(venv) $ python manage.py loaddata data.json --settings=fitness_api.settings.development
```

5) Запустите приложение

```sh
(venv) $ python manage.py runserver --settings=fitness_api.settings.development
```

## Документация (swagger)

Чтобы открыть документацию пройдите по пути http://127.0.0.1:8000/swagger/ или http://127.0.0.1:8000/redoc/

<img src="media/swagger.png" width="1200" />

## Структура базы данных

Я использовал таблицу Users, предоставляемую Джанго, чтобы у всех пользователей был функционал аутентификации и функционал другого, что предоставляет Джанго. Я ее модифицировали, чтобы добавить недостающие поля middlename, dateofbirth, gender. А пользователей по ролям я разделил с помощью связи One-to-one с таблицей Users.

Информация о расписание тренеров хранится в таблице trainer_schedule, а информация о расписание занятий храниться в таблице clients_chedule.

Примерная получившейся база данных.

<img src="media/db-structure.png" width="1200" />
