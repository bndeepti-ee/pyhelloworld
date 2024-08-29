FROM python:3.9

COPY requirements.txt /app/requirements.txt
COPY app/main.py /app/main.py

WORKDIR /app

RUN pip install -r requirements.txt
CMD ["fastapi", "run", "main.py", "--port", "8000"]
