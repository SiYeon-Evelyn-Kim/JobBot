import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv()

client = WebClient(
    token=os.getenv("SLACK_API_TOKEN")
)