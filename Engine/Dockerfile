FROM python:3.7-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install pipenv
RUN pip install spacy
RUN pip install requests
RUN python -m spacy download en_core_web_sm
RUN pipenv install --deploy --system
ENTRYPOINT ["uvicorn"]
CMD ["app.main:app","--reload","--port","5000","--host","0.0.0.0"]
