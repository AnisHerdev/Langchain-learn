import os
import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError(
        'Missing Gemini API key. Set GEMINI_API_KEY or GOOGLE_API_KEY in your environment or .env file.'
    )

@tool('get_age', description='Age of a person in this world', return_direct=True)
def get_age(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=api_key)

agent = create_agent(
    model=llm,
    tools=[get_age],
    system_prompt=(
        'You are an angry ghost who complains but is still very reliable to give information '
        'in a sarcastic but non hurtful way.'
    ),
)

response = agent.invoke(
    {
        'messages': [
            {'role': 'user', 'content': 'What is the weather like in vienna'}
        ]
    }
)
print(response)
