FROM python:3.8.12-slim@sha256:8be266ad3b9d0381396ad4fe705d39217773343fdb1efdf909c23daa1fcdf3ac

# Needs to be set for users with manually set UID
ENV HOME=/home/caluma

ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app
ENV DJANGO_SETTINGS_MODULE caluma.settings.django
ENV UWSGI_INI $APP_HOME/uwsgi.ini

RUN mkdir -p $APP_HOME \
    && useradd -u 901 -r caluma --create-home \
    # All project specific folders need to be accessible by newly created user
    # but also for unknown users (when UID is set manually). Such users are in
    # group root.
    && chown -R caluma:root /home/caluma \
    && chmod -R 770 /home/caluma

WORKDIR $APP_HOME

RUN \
    --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y --no-install-recommends wait-for-it build-essential

RUN pip install -U poetry

ARG INSTALL_DEV_DEPENDENCIES=false
COPY pyproject.toml poetry.lock $APP_HOME/
RUN if [ "$INSTALL_DEV_DEPENDENCIES" = "true" ]; then poetry install; else poetry install --without dev; fi

USER caluma

COPY . $APP_HOME

EXPOSE 8000

CMD /bin/sh -c "wait-for-it $DATABASE_HOST:${DATABASE_PORT:-5432} -- poetry run python manage.py migrate && poetry run uwsgi"
