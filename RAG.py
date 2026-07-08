from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# model = init_chat_model(model='gemini-2.5-flash-lite',temperature=0.7,model_provider='google-genai')

if __name__ == "__main__":
    texts=[
        'Hello can i please have an apple',
        'I just got an expensive gift for my friend from apple.',
        'Please show me the nearest coffee shop',
        'Can you help me find a good book',
        'I need simple directions to the train station',
    ]

    vector_store = FAISS.from_texts(texts,embedding=embeddings)

    for ele in vector_store.similarity_search('I want some beverage.',k=3):
        print(ele)
    print()
    for ele in vector_store.similarity_search('I want an iphone.',k=3):
        print(ele)