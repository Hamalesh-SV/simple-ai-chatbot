# AI Chatbot using Streamlit and Ollama

## Project Description

This project is a simple AI-powered chatbot built using Streamlit and Ollama. It allows users to interact with an AI assistant through a web-based chat interface.

The chatbot uses the Llama 3.2 model to generate responses and maintains conversation history using Streamlit session state. It also supports streaming responses, displaying answers word by word as they are generated.

## Features

* Interactive chat interface using Streamlit.
* Powered by the Llama 3.2 language model.
* Maintains conversation history.
* Generates real-time streaming responses.
* Uses a system prompt to guide AI responses.
* Runs locally using Ollama.

## Technologies Used

* Python
* Streamlit
* Ollama
* Llama 3.2

## Project Structure

```text
AI-Chatbot/
│
├── chatbot.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <https://github.com/Hamalesh-SV/simple-ai-chatbot>
```

### Step 2: Navigate to the Project Folder

```bash
cd AI-Chatbot
```

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv myenv
```

Activate the environment on Windows:

```bash
myenv\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Install Ollama

Download and install Ollama from its official website:

https://ollama.com/

### Step 6: Download the Llama 3.2 Model

Open Command Prompt or Terminal and execute:

```bash
ollama pull llama3.2
```

### Step 7: Run the Chatbot

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default browser.

## How It Works

1. The user enters a question in the Streamlit chat interface.
2. The application stores the conversation in Streamlit session state.
3. The conversation history is passed to the Llama 3.2 model through Ollama.
4. Ollama generates a response.
5. The response is streamed and displayed in real time.
6. The assistant's response is saved in the conversation history.

## AI Model

**Llama 3.2**

The Llama 3.2 model is used to understand user questions and generate natural language responses locally through Ollama.

## Future Improvements

* Add PDF and document-based question answering.
* Implement chat history download.
* Add support for multiple Ollama models.
* Improve the chatbot interface.
* Add a RAG-based knowledge retrieval system.

## Author

Developed as a Python Generative AI project.
