FROM python:3.8-alpine

COPY . /app

WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt 


EXPOSE 8000

CMD ["/opt/venv/bin/gunicorn","--workers", "3","--worker-tmp-dir", "/dev/shm", "backend.wsgi:application", "--bind",":8000"]



