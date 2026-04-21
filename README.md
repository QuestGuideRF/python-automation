# 🐍 Python Automation

<p align="center">
  <b>Коллекция мощных инструментов автоматизации на Python для различных задач</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python" alt="Python Version">

</p>

---

## 📋 Описание

**Python Automation** — это комплексная коллекция скриптов и утилит для автоматизации различных задач: от работы с базами данных и облачными сервисами до веб-скрапинга и генерации контента. Проект идеально подходит для разработчиков, DevOps-инженеров и всех, кто хочет оптимизировать свою работу с помощью Python.

---

## ✨ Основные возможности

### 🗄️ **Автоматизация баз данных**
- Подключение к MySQL
- Извлечение и обработка данных
- Сортировка и фильтрация результатов

### ☁️ **Облачные сервисы**
- Работа с GitHub API (ветки, коммиты, репозитории)
- Интеграция с Kubernetes (мониторинг подов, экспорт данных)
- Управление инфраструктурой

### 🌐 **Веб-автоматизация**
- Скрапинг веб-сайтов
- Генерация QR-кодов
- Тестирование API эндпоинтов

### 🔐 **Безопасность и утилиты**
- Генератор паролей с графическим интерфейсом
- Генерация OTP кодов
- Отправка email через Gmail

### 🎤 **Обработка контента**
- Преобразование текста в речь (TTS)
- Чтение PDF файлов
- Работа с файлами и документами

### 📊 **Анализ данных**
- Анализ новостей с использованием машинного обучения
- Сравнение и сортировка списков
- Обработка данных

---

## 📁 Структура проекта

```
python_automation/
├── DB_Automation.py          # Автоматизация работы с MySQL
├── Github.py                  # Работа с GitHub API
├── kubernetes_Access.py       # Интеграция с Kubernetes
│
├── Python/                    # Основные Python утилиты
│   ├── finalmail.py          # Отправка email через Gmail
│   ├── NEWS.py               # Анализ новостей (ML)
│   ├── OTP_VERIFICATION.py   # Генерация OTP кодов
│   ├── PASSWORD_GENERATOR.py # Генератор паролей (GUI)
│   ├── QR_CODE_WORKING.py    # Генерация QR-кодов
│   └── SCRAPE_WEBSITE_WORKING.py  # Веб-скрапинг
│
├── Python-Speech/            # Работа с речью и файлами
│   ├── SPEECH.py             # TTS и чтение PDF
│   ├── SLIDES_PYTHON.py      # Обучающие примеры
│   └── FILE_HANDLING.py      # Работа с файлами
│
└── Org_Automation/           # Организационная автоматизация
    ├── Compare_list.py       # Сравнение списков
    ├── Endpoint_Hit.py       # Тестирование API
    └── List_with_sort.py     # Сортировка данных
```

---

## 🚀 Быстрый старт

### Установка зависимостей

```bash
# Основные зависимости
pip install mysql-connector-python requests pandas kubernetes beautifulsoup4

# Для работы с речью
pip install pyttsx3 PyPDF2

# Для генерации QR-кодов
pip install pyqrcode

# Для GUI генератора паролей
pip install pyperclip

# Для машинного обучения
pip install scikit-learn numpy pandas
```

### Использование

Каждый скрипт можно запускать независимо:

```bash
# Работа с базой данных
python DB_Automation.py

# Работа с GitHub
python Github.py

# Доступ к Kubernetes
python kubernetes_Access.py

# Генератор паролей
python Python/PASSWORD_GENERATOR.py
```

---

## 📖 Детальное описание модулей

### 🗄️ DB_Automation.py
**Автоматизация работы с MySQL**

- Подключение к базе данных MySQL
- Выполнение SQL-запросов
- Извлечение данных из таблиц
- Сортировка результатов по заданным колонкам

**Пример использования:**
```python
# Настройте параметры подключения
host = 'localhost'
user = 'root'
password = 'yourpassword'
database = 'yourdatabase'

# Скрипт автоматически подключится и выполнит запрос
```

---

### 🐙 Github.py
**Работа с GitHub API**

- Получение списка веток репозитория
- Извлечение информации о коммитах
- Проверка защищенных веток
- Фильтрация и сортировка веток

**Возможности:**
- Получение SHA коммитов
- Определение защищенных веток
- Фильтрация по паттернам (например, только feature-ветки)
- Сортировка по алфавиту

---

### ☸️ kubernetes_Access.py
**Интеграция с Kubernetes**

- Подключение к кластеру Kubernetes
- Получение информации о всех подах
- Экспорт данных в CSV
- Анализ данных с помощью Pandas

**Экспортируемые данные:**
- Namespace
- Имя пода
- Статус
- Дата создания
- Имя ноды

---

### 📧 Python/finalmail.py
**Отправка email через Gmail**

Простой скрипт для отправки электронных писем через SMTP сервер Gmail.

**Настройка:**
```python
gmail_user = "your-email@gmail.com"
gmail_pwd = "your-password"
TO = 'recipient@gmail.com'
```

---

### 📰 Python/NEWS.py
**Анализ новостей с машинным обучением**

Использует библиотеку scikit-learn для анализа новостных данных:
- Загрузка данных из CSV
- Векторизация текста (TF-IDF)
- Классификация с помощью PassiveAggressiveClassifier
- Оценка точности модели

---

### 🔐 Python/OTP_VERIFICATION.py
**Генерация OTP кодов**

Генерирует 6-значные одноразовые пароли для верификации.

---

### 🔑 Python/PASSWORD_GENERATOR.py
**Генератор паролей с GUI**

Графический интерфейс для генерации безопасных паролей:
- Настраиваемая длина пароля
- Использование букв (верхний/нижний регистр), цифр и спецсимволов
- Автоматическое копирование в буфер обмена

---

### 📱 Python/QR_CODE_WORKING.py
**Генерация QR-кодов**

Создает QR-коды для URL, текста или других данных:
- Поддержка SVG формата
- Настраиваемый масштаб
- Простое использование

---

### 🕷️ Python/SCRAPE_WEBSITE_WORKING.py
**Веб-скрапинг**

Класс для извлечения данных с веб-сайтов:
- Парсинг HTML
- Поиск ссылок по паттернам
- Извлечение статей и контента

---

### 🎤 Python-Speech/SPEECH.py
**Преобразование текста в речь**

- Чтение PDF файлов вслух
- Преобразование текста в аудио (MP3/WAV)
- Использование библиотеки pyttsx3

---

### 📚 Python-Speech/SLIDES_PYTHON.py
**Обучающие примеры Python**

Комплексная коллекция примеров для изучения Python:
- Переменные и типы данных
- Строки, списки, кортежи, словари
- Условные операторы и циклы
- Функции и рекурсия
- ООП (классы, наследование)
- JSON обработка
- Обработка исключений

---

### 📄 Python-Speech/FILE_HANDLING.py
**Работа с файлами**

Базовые операции с файлами:
- Создание файлов
- Чтение файлов
- Запись в файлы
- Добавление данных (append)

---

### 🔍 Org_Automation/Compare_list.py
**Сравнение списков**

Утилита для сравнения и анализа списков версий:
- Парсинг версий из строк
- Поиск дубликатов
- Сравнение элементов

---

### 🌐 Org_Automation/Endpoint_Hit.py
**Тестирование API эндпоинтов**

Автоматическое тестирование API:
- Получение списка эндпоинтов
- Проверка доступности каждого эндпоинта
- Обработка таймаутов
- Фильтрация по статус-кодам

---

### 📊 Org_Automation/List_with_sort.py
**Сортировка данных**

Обработка и сортировка числовых списков:
- Вычисление квадратов чисел
- Сортировка результатов
- Валидация входных данных

---

## 🛠️ Технологии

| Категория | Технологии |
|:---------:|:----------:|
| **Язык** | Python 3.6+ |
| **Базы данных** | MySQL (mysql-connector-python) |
| **Веб** | Requests, BeautifulSoup4, urllib |
| **Облако** | Kubernetes Python Client |
| **ML/AI** | scikit-learn, NumPy, Pandas |
| **GUI** | Tkinter |
| **Медиа** | pyttsx3, PyPDF2, pyqrcode |
| **Утилиты** | pyperclip, json, csv |

---

## 📝 Требования

- Python 3.6 или выше
- Доступ к интернету (для работы с API)
- MySQL сервер (для DB_Automation)
- Kubernetes кластер (для kubernetes_Access)
- GitHub токен (опционально, для увеличения лимитов API)

---

## 🔧 Настройка

### MySQL (DB_Automation.py)
```python
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database'
```

### GitHub (Github.py)
```python
owner = "your-username"
repo = "your-repo"
headers = {
    "Authorization": "token your-github-token"
}
```

### Kubernetes (kubernetes_Access.py)
Убедитесь, что файл `~/.kube/config` настроен правильно или скрипт запущен внутри кластера.

---

## 💡 Примеры использования

### Генерация пароля
```bash
python Python/PASSWORD_GENERATOR.py
# Откроется окно, введите длину пароля и нажмите "Generator"
```

### Создание QR-кода
```python
import pyqrcode
url = pyqrcode.create("https://example.com")
url.svg("qrcode.svg", scale=8)
```

### Отправка email
```python
# Настройте учетные данные в finalmail.py
python Python/finalmail.py
```

---
Автор: legenda_god
Telegram: https://t.me/FitoDomik