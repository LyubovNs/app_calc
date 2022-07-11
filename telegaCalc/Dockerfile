# указание базового образа onbuild
FROM python:latest

# выбор рабочей директории
WORKDIR /usr/src/app

# копирование нужного файла в рабочую директорию
COPY CheckSalary_v2.py ./

# обновить pip
RUN pip install --upgrade pip

# добавить пользователя, от которого будут выполняться команды
RUN adduser myuser
USER myuser

# поменять пользователя, от которого будут выполняться команды
COPY --chown=myuser:myuser requirements.txt requirements.txt

# запуск от пользователя USER
RUN pip install --user -r requirements.txt

# запуск скрипта
CMD ["python", "./CheckSalary_v2.py"]