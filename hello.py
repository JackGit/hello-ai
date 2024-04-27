import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('KEY')

from openai import OpenAI
client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Who won the world series in 2020?."}
  ]
)

print(completion.choices[0].message)