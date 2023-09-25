FROM python:3.11

# ENV PYTHONFAULTHANDLER=1 \
#     PYTHONUNBUFFERED=1 \
#     PYTHONHASHSEED=random \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100 \

RUN pip install poetry==1.6.1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi -vvv

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python", "run.py"]