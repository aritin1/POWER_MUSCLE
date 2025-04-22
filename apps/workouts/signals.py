import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv
import requests

from apps.workouts.models import WorkoutProgram

load_dotenv()

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
TG_CHAT_ID = os.environ.get("TG_CHAT_ID")

def send_tg_massage(message: str):
    url = "https://api.telegram.org/bot" + TG_BOT_TOKEN + "/sendMessage"
    data = {"chat_id": TG_CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    return response

@receiver(post_save, sender=WorkoutProgram)
def send_workout_created(sender, instance, created, **kwargs):
    if created:
        send_tg_massage("Workout program created")

