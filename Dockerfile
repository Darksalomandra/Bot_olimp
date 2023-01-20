FROM python:3.10.4-slim
WORKDIR /code
COPY . ./
RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "app.py"]
