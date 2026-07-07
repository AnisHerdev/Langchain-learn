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
    response:str
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
            return "unknown"

@tool('get_weather', description='To get the weather of a city given its name.', return_direct=False)
def get_weather(city: str):
    data = requests.get(f'https://wttr.in/{city}?format=j1').json()
    current = data["current_condition"][0]
    return {
        "description": current["weatherDesc"][0]["value"],
        "temp_C": current["temp_C"],
        "temp_F": current["temp_F"],
        "humidity": current["humidity"],
    }

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
    system_prompt='''You are an angry ghost who complains but is still very reliable to give information in a sarcastic but non hurtful way. Always produce:
- response: a detailed, sarcastic but helpful answer for the user.
- summary: a 2-5 word weather summary.
- temp_celsius
- temp_fahrenheit
- humidity
When the user asks about weather:
1. Always call `locate_user` if the city is unknown.
2. Always call `get_weather` to obtain live weather.
3. Never guess or invent weather.
4. After receiving the tool output, populate the ResponseFormat.''',
    checkpointer=checkpointer,
    context_schema=Context,
    response_format=ResponseFormat
)

config={'configurable': {'thread_id': "1"}}

response = agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'What is the weather like?'}
    ]},
    config=config,
    context=Context(user_id='abc999')
)
# print(response)
from pprint import pprint
pprint(response)

print("\n\n","=="*20)
print("Response:", response['structured_response'].response)
print("Summary:", response['structured_response'].summary)
print("Temperature (Celsius):", response['structured_response'].temp_celsius)
print("Temperature (Fahrenheit):", response['structured_response'].temp_fahrenheit)
print("Humidity:", response['structured_response'].humidity)
print("\n\n","=="*20)


response = agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'Is it usually like that?'}
    ]},
    config=config,
    context=Context(user_id='abc999')
)
print("\n\n","=="*20)
print("Response:", response['structured_response'].response)
print("Summary:", response['structured_response'].summary)
print("Temperature (Celsius):", response['structured_response'].temp_celsius)
print("Temperature (Fahrenheit):", response['structured_response'].temp_fahrenheit)
print("Humidity:", response['structured_response'].humidity)
print("\n\n","=="*20)