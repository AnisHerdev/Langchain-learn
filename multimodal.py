from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from base64 import b64encode

load_dotenv()
model = init_chat_model(model='gemini-2.5-flash',temperature=0.7, model_provider="google-genai")

message={
    'role':'user',
    'content':[
        {'type':'text','text':'Descibe this image to a 5 year old.'},
        {'type':'image','base64':b64encode(open('buddhist-monk.jpg','rb').read()).decode(), 'mime_type':'image/jpg'}
    ]
}

response = model.invoke([message])
print(response.content)