import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","1175195444:AAHifP4wb2HJPCvD_Fqph9YdCwSyiRyVtf8")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","d9bcc1c9-5cc8-4373-b684-125dab6553b3")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","")
