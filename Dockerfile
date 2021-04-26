FROM python:3.8-alphine
ENV PATH="/scripts/${PATH}"
COPY ./requirement.txt  ./requirement.txt
RUN apk add --update-no-cache --virtual .tmp gcc libc-dev linux-headers
RUN  pip install -r /requirement.txt
RUN apk del .tmp
RUN mkdir  /app
COPY ./backend /app
COPY ./media /app
COPY ./roza /app
WORKDIR /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*
RUN mkdir -/vol/web/media
RUN mkdir -/vol/web/static
RUN adduser -D user
RUN chown user:user /vol
RUN chmod -R 755 /vol/web
USER user
CMD ["entrypoint.sh"]