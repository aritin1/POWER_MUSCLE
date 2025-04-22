import os

import requests
from celery import shared_task
from dotenv import load_dotenv
from apps.workouts.models import WorkoutProgram

load_dotenv()

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
TG_CHAT_ID = os.environ.get("TG_CHAT_ID")



@shared_task()
def send_tg():
    url = "https://api.telegram.org/bot" + TG_BOT_TOKEN + "/sendMessage"
    data = {"chat_id": TG_CHAT_ID, "text": f"{WorkoutProgram.user} Создал программу тренировок"}
    response = requests.post(url, json=data)
    return response