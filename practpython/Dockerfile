# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /pythonProject

# Копируем файлы requirements.txt и скрипт python в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# Запускаем скрипт при запуске контейнера
CMD ["python", "pythonProject/main.py"]