from dotenv import load_dotenv
import os

load_dotenv(".env")
print(os.getenv('BOT_TOKEN'))
os.environ.setdefault('wdqdfbhu','Hello')
print(os.getenv('wdqdfbhu'))