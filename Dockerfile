FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.6.1

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
WORKDIR src