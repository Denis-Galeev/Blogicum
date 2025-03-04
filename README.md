# Проект Blogicum <img src="blogicum/static_dev/img/logo.png" width="40"/>

**Blogicum** — это удобная платформа на **Django** для ведения личных блогов. Пользователи могут создавать и редактировать и удалять посты, добавлять фотографии к ним, а также оставлять комментарии. Поддерживаются отложенные публикации, которые видны только авторам. Контент организован по категориям, что облегчает навигацию, а встроенная пагинация делает просмотр удобным.

## Функции:

- **Посты:** У зарегистрированных пользователей есть возможность создавать, редактировать и удалять свои записи, есть поддержка категорий.
- **Отложенная публикация:** Возможность указать дату публикации «в будущем», можно создавать отложенные посты.
- **Комментарии:** На странице поста под текстом записи есть возможность оставлять, редактировать и удалять комментарии (только для авторизованных пользователей).
- **Профиль:** Настраиваемый профиль с информация о пользователе и публикациями пользователя (доступно всем посетителям). Редактирование профиля для изменения имени, фамилии, логина, адреса электронной почты и изменения пароля (доступно только залогиненному пользователю — хозяину аккаунта),
- **Аутентификация:** Регистрация, вход и смена и восстановление пароля через e-mail.
- **Админ-панель:** Удобное управление контентом и пользователями через кастомизированную админ-панель Django. Новые категории и местоположения может создавать только администратор сайта через панель администратора. Возможность снять с публикации пост, комментарий или категорию.
- **Кастомные страницы для ошибок:** 403 CSRF, 404 и 500.
- **Пагинация:** В проекте подключена и настроена пагинация — вывод не более 10 публикаций на главной странице, на странице пользователя, на странице категории.

## Используемые технологии:
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## Системные требования

- **[Python](https://www.python.org/downloads/) 3.9 или выше.**
- **Операционная система: Windows / macOS / Linux**
- **SQLite: [sqlite3](https://www.sqlite.org/)**

## Как запустить проект:

### 1. Клонировать репозиторий и перейти в него:
```bash
git clone git@github.com:Denis-Galeev/django_sprint4.git
```
```bash
cd django_sprint4
```

### 2. Cоздать и активировать виртуальное окружение, установить зависимости, обновить pip:
- **Windows**
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
```bash
python -m pip install --upgrade pip
```
- **Linux/Mac**
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 -m pip install --upgrade pip
```

### 3. Создать и примененить миграций:
- **Windows**
```bash
python blogicum/manage.py makemigrations
```
```bash
python blogicum/manage.py migrate
```
- **Linux/Mac**
```bash
python3 blogicum/manage.py makemigrations
```
```bash
python3 blogicum/manage.py migrate
```

### 4. Загрузить данные из фикстур:
- **Windows**
```bash
python blogicum/manage.py loaddata db.json
```
- **Linux/Mac**
```bash
python3 blogicum/manage.py loaddata db.json
```

### 5. Создать суперпользователя (если необходимо):
- **Windows**
```bash
python blogicum/manage.py createsuperuser
```
- **Linux/Mac**
```bash
python3 blogicum/manage.py createsuperuser
```

### 6. Запуск сервера:
- **Windows**
```bash
python blogicum/manage.py runserver
```
- **Linux/Mac**
```bash
python3 blogicum/manage.py runserver
```

### 7. Перейти на локальный сервер:

| Адрес | Описание |
|-------------|-------------|
| **http://127.0.0.1:8000/**   | **Главная страница**   |
| **http://127.0.0.1:8000/admin/**   | **Панель администратора**  |

## Автор:

**Имя:** Денис Галеев  
**Почта:** dmdenis74chel@yandex.ru  
**Telegram:** @Denis_74_chel  