FROM python

RUN pip install requests

RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN echo "Europe/Paris" > /etc/timezone

COPY ./app /app
WORKDIR /app

CMD ["python3", "main.py"]
