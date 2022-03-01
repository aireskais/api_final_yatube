# Описание проекта:
Апи социальной сети для публикации личных дневников. Позволяет работать с постами, комментариями к ним, группами и подписчиками

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/aireskais/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
# Примеры запросов
Локументация:
- /redoc/

Получить все посты:
- /api/v1/posts/

Получить все комментарии к посту 1
- /api/v1/posts/1/comments/
