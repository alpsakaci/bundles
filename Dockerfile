FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY spPassphrase.txt /etc/spPassphrase.txt

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
