FROM python:3.14.0-alpine3.22
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY src ./src
EXPOSE 5000
RUN useradd app
USER app


CMD ["python", "app.py"]