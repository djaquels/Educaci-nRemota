FROM python:3.7-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN mkdir -p /src/files/app
RUN chmod -R 777 /app/app/storage
RUN pip install pipenv
RUN pip install --upgrade ibm-watson
RUN pipenv install --deploy --system
ENTRYPOINT ["uvicorn"]
CMD ["app.main:app","--reload","--port","5000","--host","0.0.0.0"]

