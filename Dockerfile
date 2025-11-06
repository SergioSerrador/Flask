FROM python:3.14.0-alpine3.22
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
RUN adduser -D app
USER app
CMD ["python", "app.py"]