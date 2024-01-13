FROM python

# установить каталог для приложения
WORKDIR .

# копировать все файлы в контейнер
COPY . .

# установка зависимостей
RUN pip install --no-cache-dir -r requerements

# ENV TZ 

# какой порт должен экспоузить контейнер - декларация - нужно прокидывать все равно
EXPOSE 5000

# запуск команды
CMD ["python", "./main.py"]