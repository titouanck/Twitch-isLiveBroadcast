FROM python

RUN pip install requests bs4 twitchio

COPY ./app /app
WORKDIR /app

CMD ["python3", "main.py"]
