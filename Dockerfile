FROM python:latest

# установить каталог для приложения
WORKDIR /usr/src/app

# копировать все файлы в контейнер
COPY . /usr/src/app


# установка зависимостей
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requerements

# ENV TZ 

# какой порт должен экспоузить контейнер - декларация - нужно прокидывать все равно
EXPOSE 5000

# запуск команды
CMD ["python", "main.py"]