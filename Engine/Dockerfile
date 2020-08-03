FROM python:3.7-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install pipenv
RUN pip install spacy
RUN python -m spacy download en_core_web_sm
RUN pipenv install --deploy --system
CMD exec gunicorn --bind :5000 --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app
