FROM python:3.8

# установить каталог для приложения
WORKDIR .

# копировать все файлы в контейнер
COPY . .

# установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

ENV TZ 

# какой порт должен экспоузить контейнер - декларация - нужно прокидывать все равно
EXPOSE 5000

# запуск команды
CMD ["python", "./manage.py", "runserver", "0.0.0.0:5000"]