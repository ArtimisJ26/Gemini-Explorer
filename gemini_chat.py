import vertexai  # Import the Vertex AI SDK to interact with Google's AI models
import streamlit as st  # Import Streamlit to create the web interface
from vertexai.preview import generative_models  # Import generative models from Vertex AI
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession  # Import specific components needed for generative AI chat
from secret import *

# Initialize Vertex AI with the specified project ID (replace with your actual Google Cloud project ID)
project = project_id
vertexai.init(project=project)

# Define the configuration for the AI model, setting parameters such as temperature (controls randomness of responses)
config = generative_models.GenerationConfig(
    temperature=0.4  # Lower values make responses more deterministic, higher values add variability
)

# Load the AI model with the specified configuration
model = GenerativeModel(
    "gemini-2.0-flash-exp",  # Specifies the AI model to be used (Google Gemini Pro)
    generation_config=config  # Apply the previously defined configuration
)

# Start a chat session with the model
chat = model.start_chat()

# Define a function to send user queries to the AI and display responses

def llm_function(chat: ChatSession, query):
    """Sends a query to the AI model and processes the response."""
    response = chat.send_message(query)  # Send the user's query to the chat session
    output = response.candidates[0].content.parts[0].text  # Extract the response text

    # Display the AI's response in Streamlit's chat interface
    with st.chat_message("model"):
        st.markdown(output)  # Show the response using Markdown formatting

    # Store user input in the session state for chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    # Store AI's response in the session state for chat history
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

# Set the title of the Streamlit web app
st.title("Gemini Explorer")

# Initialize chat history in session state if it does not exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Iterate through past chat messages and display them
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role=message["role"],  # Assign role (either 'user' or 'model')
        parts=[Part.from_text(message["content"])]  # Store message content
    )
    
    if index != 0:  # Skip displaying the first message to prevent duplication
        with st.chat_message(message["role"]):
            st.markdown(message["content"])  # Display past messages in chat format
    
    chat.history.append(content)  # Append message to chat history for context

# If chat history is empty, send an initial message to the user
if len(st.session_state.messages) == 0:
    initial_prompt = "Ask the user their name and information. Address the user by their name after that. Adapt to their style and talking and reply in the same manner"
    llm_function(chat, initial_prompt)  # AI starts the conversation with the user

# Capture user input via a chat input box
query = st.chat_input("Gemini Explorer")

# Process user input when they enter a message
if query:
    with st.chat_message("user"):
        st.markdown(query)  # Display the user's input in chat format
    llm_function(chat, query)  # Send the user's message to the AI model
