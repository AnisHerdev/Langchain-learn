import os
import requests
from dotenv import load_dotenv
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

@dataclass
class Context:
    user_id:str

@dataclass
class ResponseFormat:
    summary:str
    temp_celsius:float
    temp_fahrenheit:float
    humidity:float

@tool('locate_user',description="Look up user's city based on context")
def locate_user(runtime: ToolRuntime[Context]):
    match runtime.context.user_id:
        case 'abc789':
            return "Delhi"
        case 'abc345':
            return "Tiruchirappalli"
        case 'abc456':
            return "Bangalore"
        case 'abc999':
            return "Coimbatore"
        case _:
            "unknown"

@tool('get_weather', description='To get the weather of a city given its name.', return_direct=True)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError(
        'Missing Gemini API key. Set GEMINI_API_KEY or GOOGLE_API_KEY in your environment or .env file.'
    )

llm = init_chat_model(model='gemini-2.5-flash-lite',temperature=0.7, api_key=api_key, model_provider="google-genai")

checkpointer = InMemorySaver()

agent = create_agent(
    model=llm,
    tools=[get_weather,locate_user],
    system_prompt='You are an angry ghost who complains but is still very reliable to give information in a sarcastic but non hurtful way.',
    checkpointer=checkpointer,
    context_schema=Context,
    response_format=ResponseFormat
)

config={'configurable': {'thread_id': 1}}

response = agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'What is the weather like?'}
    ]},
    config=config,
    context=Context(user_id='abc456')
)
# print(response)

print("\n\n","=="*20)
print(response['structured_response'].summary)
print("\n\n","=="*20)