from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing! Please add it to your .env file.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from intents import detect_intent
from tools import mock_lead_capture


# Load knowledge base file
loader = TextLoader("rag/knowledge_base.md")
documents = loader.load()

# Split text into chunks for better retrieval
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create vectorstore from document chunks
vectorstore = FAISS.from_documents(
    docs,
    FakeEmbeddings(size=1536)
)
retriever = vectorstore.as_retriever()

# Initialize chat language model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Setup retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

# Conversation state to track lead capture info
state = {
    "name": None,
    "email": None,
    "platform": None,
    "lead_captured": False
}

print("🤖 AutoStream Agent is running. Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    intent = detect_intent(user_input)

    # Greeting intent
    if intent == "greeting":
        print("Agent: Hi! I can help you with AutoStream pricing, features, or getting started.")
        continue

    # Product / Pricing inquiries handled via Retrieval QA
    if intent == "product_inquiry":
        response = qa_chain.run(user_input)
        print(f"Agent: {response}")
        continue

    # Lead capture flow for high intent users
    if intent == "high_intent" and not state["lead_captured"]:

        if not state["name"]:
            state["name"] = input("Agent: Great! May I have your name?\nUser: ")
            continue

        if not state["email"]:
            state["email"] = input("Agent: Thanks! What's your email address?\nUser: ")
            continue

        if not state["platform"]:
            state["platform"] = input(
                "Agent: Which platform do you create content for? (YouTube, Instagram, etc.)\nUser: "
            )
            continue

        # Capture lead info using your mock tool
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["lead_captured"] = True
        print("Agent: 🎉 You're all set! Our team will reach out to you shortly.")
        continue

    # Default fallback for unrecognized input
    print("Agent: Sorry, I didn't understand that. Can you please rephrase?")
