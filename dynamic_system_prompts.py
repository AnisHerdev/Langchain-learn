from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.agents.middleware import ModelRequest,ModelResponse,dynamic_prompt
from dataclasses import dataclass

load_dotenv()


@dataclass
class Context:
    user_role:str

@dynamic_prompt
def user_role_prompt(request: ModelRequest)->str:
    user_role = request.runtime.context.user_role
    base_prompt = "You are a helpful and very concise assistant."
    match user_role:
        case 'expert':
            return base_prompt+" You have extensive knowledge in your field. And provides detailed and technical explanations."
        case 'beginner':
            return base_prompt+" provides simple and easy to understand explanations."
        case 'child':
            return base_prompt+" provides explanations suitable for a 5 year old child."
        case _:
            return "unknown"

model = init_chat_model(model="gemini-2.5-flash-lite",temperature=0.5,model_provider="google_genai")

agent= create_agent(
    model=model,
    middleware=[user_role_prompt],  
    context_schema=Context
)

for role in ['expert','beginner','child']:
    response = agent.invoke({
        'messages':[{'role':'user','content':'Explan quantum computing.'}]
    },  context=Context(user_role=role)
    )

    print(f"Role : {role}".center(50,'-'))
    print(response)