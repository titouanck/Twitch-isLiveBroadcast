FROM python

RUN pip install requests bs4 twitchio
COPY bot.py /root/bot.py
WORKDIR /root

CMD ["python3", "bot.py"]
