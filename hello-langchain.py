import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('KEY')

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key=API_KEY)
print(llm.invoke("how can langsmith help with testing?"))