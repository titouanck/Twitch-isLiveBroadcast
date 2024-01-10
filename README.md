### What does it do ? How does it work ?
The program will use the .json files provided, and launch X docker containers, each based on a file.  
In each container, a python program performs the following pseudo-code:  
```python
when CHANNEL_TO_MONITOR goes live:
  for MESSAGE in MESSAGES_TO_SEND:
    send MESSAGE on the chat of CHANNEL_TO_SEND_MESSAGE
    time.sleep(COOLDOWN_BETWEEN_MESSAGES)
```

### Clone the project
```bash
git clone https://github.com/titouanck/Twitch-messageOnLive.git
cd Twitch-messageOnLive
```

### Set-up the project
Inside the `configurations/` directory, you will find multiple files ending with the extension **.JSON**.  

  
To get started, you can take a look at any of the **.JSON** file present in the directory.  
For example, with `kyzen_.json` I want to send two defined messages on kyzen_'s chat when he goes live on Twitch:

|           |           |
|-----------|-----------|
| <img width="276" alt="Screenshot 2024-01-10 at 18 55 19" src="https://github.com/titouanck/Twitch-messageOnLive/assets/87268044/12aa421c-2e02-44df-b115-ec335e698089"> | <img width="548" alt="Screenshot 2024-01-10 at 19 26 43" src="https://github.com/titouanck/Twitch-messageOnLive/assets/87268044/a4daee1a-b7c4-469f-b92f-3b45ce83da05">
