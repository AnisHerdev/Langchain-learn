import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool

@tool('get_age',description="Age of a person in this world", return_direct=True)
def get_age(city: str):
    response = request.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

agent = create_agent(
    model='gemini-2.0-flash',
    tools=[get_age],
    system_prompt= 'You are an angry ghost who complains but is still very reliable to give information in a sarcastic but non hurtful way.'
)

response = agent.invoke({
    'message':{
        {'role': 'user', 'content': 'What is the weather like in vienna'}
    }
})