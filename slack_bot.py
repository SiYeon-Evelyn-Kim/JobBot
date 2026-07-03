import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv()  # .env 파일 내용을 불러오는 코드

slack_token = os.environ.get("SLACK_API_TOKEN")
client = WebClient(token=slack_token)

client.chat_postMessage(
    channel="#공고목록",
    text="안녕하세요! 봇 테스트입니다."
)