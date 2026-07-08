from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.tools import create_retriever_tool
from langchain.agents import create_agent

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
model = init_chat_model(model='gemini-2.5-flash',temperature=0.7,model_provider='google-genai')


if __name__ == "__main__":
    texts=[
        'I woke up excited for a day trip to Jurassic Park.',
        'At the park entrance I felt a mix of awe and nervousness as towering ferns and distant roars greeted me.',
        'I saw a herd of long-necked sauropods grazing peacefully in the valley.',
        'A group of nimble raptors dashed through the underbrush, watching me with curious eyes.',
        'A massive Tyrannosaurus rex appeared on a ridge, its thunderous footsteps making the ground tremble.',
        'I ate a packed sandwich under a canopy of cycads while watching pterosaurs glide overhead.',
        'On a trail I tasted sweet berries I found, cautious but unable to resist their flavor.',
        'I felt a cold sweat when a triceratops charged nearby, then relief as it calmed and returned to grazing.',
        'The air smelled of wet earth, vegetation, and something ancient that made my skin prickle.',
        'I helped feed a gentle herbivore some leaves and felt a surprising sense of connection.',
        'At midday I sheltered from a sudden storm in a rocky overhang, listening to dinosaurs call in the rain.',
        'I watched a dramatic predator chase in the distance, heart pounding as the hunters pursued their prey.',
        'As evening fell the sky turned orange and the park grew quieter, leaving me reflective and grateful for the experience.',
        'I left the park tired but exhilarated, the images and emotions of the day replaying in my mind.',
    ]

    vector_store = FAISS.from_texts(texts,embedding=embeddings)

    retriver = vector_store.as_retriever(search_kwargs={'k':7})

    retriver_tool = create_retriever_tool(retriever=retriver, name='kb_search', description="Search a knowledge base about a person's Jurassic Park trip. "
        "Use this tool whenever questions ask about events, dinosaurs, "
        "animals, food, places, or anything the person experienced.")

    # for ele in vector_store.similarity_search('I want some beverage.',k=3):
    #     print(ele)
    # print()
    # for ele in vector_store.similarity_search('I want an iphone.',k=3):
    #     print(ele)
    agent=create_agent(
        model=model,
        tools=[retriver_tool],
        system_prompt=(
            "You are a helpful assistant. that answers what happened in one days journey of a person," \
            "first call the kb_search tool to retrive the context, then answer succinctly. You might have to go through multiple times.")
    )
    result= agent.invoke({
        'messages':[{'role':'user',"content":"What all dinosaurs did the person see?"}]
    })
    print(result)

    print("\n\n\n")
    print(result["messages"][-1].content)