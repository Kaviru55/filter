from os import environ
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

print("jjjjddadc",environ.get('SESSION'))