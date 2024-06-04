FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code

EXPOSE 80


CMD ["python", "creditManagement/manage.py", "runserver", "0.0.0.0:80"]



