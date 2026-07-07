import os
import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.chat_models import init_chat_model

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError(
        'Missing Gemini API key. Set GEMINI_API_KEY or GOOGLE_API_KEY in your environment or .env file.'
    )

@tool('get_weather', description='To get the weather of a city given its name.', return_direct=True)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

llm = init_chat_model(model='gemini-2.5-flash-lite', api_key=api_key, model_provider="google-genai")

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt=(
        'You are an angry ghost who complains but is still very reliable to give information in a sarcastic but non hurtful way.'
    ),
)

response = agent.invoke(
    {
        'messages': [
            {'role': 'user', 
            'content': 'What is the weather like in bangalore?'}
        ]
    }
)
# print(response)

print("\n\n","=="*20)
print(response['messages'][-1].content)
print("\n\n","=="*20)