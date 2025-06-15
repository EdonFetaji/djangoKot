FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python","manage.py","runserver"]
CMD ["0.0.0.0:8080"]
