FROM python:3.10-slim
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip poetry==1.6.1 && pip cache purge

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-cache

COPY . /

ENV APP_HOME /root
WORKDIR $APP_HOME
COPY /app $APP_HOME/app

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]