 API для социальной сети Yatube

## 📌 Описание проекта
RESTful API для блоговой платформы Yatube с полным набором CRUD-операций. Реализована система публикаций, комментирования и подписок на авторов.

## 🛠 Технологический стек
- **Python** 3.9+
- **Django** 3.2+
- **Django REST Framework**
- **Djoser** (JWT аутентификация)
- **SimpleJWT**
- **Pillow** (работа с изображениями)

## 🚀 Установка и запуск

### 1. Настройка окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка базы данных
```bash
python manage.py migrate
```

### 4. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 5. Запуск сервера
```bash
python manage.py runserver
```

## 🔍 Доступные эндпоинты

### 📝 Посты
| Метод | Эндпоинт              | Описание                  |
|-------|-----------------------|---------------------------|
| GET   | `/api/v1/posts/`      | Список всех постов        |
| POST  | `/api/v1/posts/`      | Создание нового поста     |
| GET   | `/api/v1/posts/{id}/` | Получение конкретного поста |

### 💬 Комментарии
```http
GET /api/v1/posts/{post_id}/comments/
Authorization: Bearer <token>
```

### 🔐 Аутентификация

#### Получение токена
```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

#### Использование токена
```http
Authorization: Bearer <your_token>
```

### 📊 Пагинация
Доступна через параметры URL:
```bash
/api/v1/posts/?limit=10&offset=20
```

## 🛠 Администрирование
Интерфейс администратора доступен по адресу:
```bash
http://localhost:8000/admin/
```

## 📄 Документация
Полная документация API доступна после запуска сервера:
```bash
http://localhost:8000/redoc/
```

---

Разработано: Максим Козлов  
2023 | Яндекс.Практикум