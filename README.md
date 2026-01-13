<!DOCTYPE html>
<html>
<head>
    <title>AutoStream Chatbot</title>
</head>
<body>

<h1>AutoStream Chatbot</h1>

<p>
This project is a simple chatbot built using Python and LangChain.
The chatbot answers product-related questions using a knowledge base
and collects user details when the user shows interest.
</p>

<h2>Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>LangChain</li>
    <li>FAISS (Vector Database)</li>
    <li>OpenAI API</li>
    <li>python-dotenv</li>
</ul>

<h2>Features</h2>
<ul>
    <li>Greets the user</li>
    <li>Answers product-related questions using a knowledge base</li>
    <li>Uses semantic search for better answers</li>
    <li>Collects name, email, and platform from interested users</li>
</ul>

<h2>Project Structure</h2>
<pre>
autostream-agent/
├── agent.py
├── intents.py
├── tools.py
├── rag/knowledge_base.md
├── .env
</pre>

<h2>How to Run the Project Locally</h2>
<ol>
    <li>Create and activate a Python virtual environment</li>
    <li>Install required libraries using pip</li>
    <li>Create a <code>.env</code> file and add the OpenAI API key</li>
    <li>Run the chatbot using <code>python agent.py</code></li>
</ol>

<h2>Architecture Explanation</h2>

<h3>Why LangChain is Used</h3>
<p>
LangChain is used to simplify interaction with language models and
to easily connect the chatbot with external data such as a knowledge base.
It helps in managing document loading, text splitting, vector search,
and response generation in a structured way.
</p>

<h3>How the Chatbot Works</h3>
<ul>
    <li>User input is first analyzed to detect intent</li>
    <li>If the intent is a product question, the chatbot searches the knowledge base</li>
    <li>Relevant information is retrieved using FAISS</li>
    <li>The language model generates a response based on retrieved data</li>
</ul>

<h3>State Management</h3>
<p>
Conversation state is managed using a simple Python dictionary.
It stores user information such as name, email, and platform.
This allows the chatbot to remember user inputs during a single session
and complete the lead capture process step by step.
</p>

<h2>Sample Questions</h2>
<ul>
    <li>Hi</li>
    <li>What is AutoStream?</li>
    <li>What features does AutoStream offer?</li>
    <li>I want to get started</li>
</ul>

<h2>WhatsApp Integration (Future Scope)</h2>
<p>
This chatbot can be integrated with WhatsApp using webhooks.
A service like Twilio WhatsApp API can be used to receive user messages.
</p>

<ul>
    <li>User sends a message on WhatsApp</li>
    <li>WhatsApp webhook forwards the message to a backend server</li>
    <li>The backend sends the message to this chatbot logic</li>
    <li>The chatbot generates a response</li>
    <li>The response is sent back to the user on WhatsApp</li>
</ul>

<p>
This approach allows the same chatbot logic to be reused across
different platforms without changing the core code.
</p>

<h2>Learning Outcomes</h2>
<ul>
    <li>Understanding of Retrieval-Augmented Generation (RAG)</li>
    <li>Hands-on experience with vector databases</li>
    <li>Knowledge of intent-based chatbot design</li>
    <li>Basic understanding of webhook-based integrations</li>
</ul>


<h2>Author</h2>
<p>
Parinita Vishwakarma
</p>

</body>
</html>
