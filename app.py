import streamlit as st
from transformers import pipeline

# Suppress warning messages from the transformers library
from transformers.utils import logging

# Set logging verbosity to error level to suppress unnecessary warnings
logging.set_verbosity_error()

# Initialize the chatbot pipeline for text-to-text generation
chatbot = pipeline(
    task="text2text-generation",  # Specifies the task type for the model
    model="facebook/blenderbot-400M-distill"  # Specifies the pre-trained model
)

# Streamlit app header
st.title("Chat with BlenderBot!")

# Define a session state variable to store the conversation history
# If it doesn't exist, initialize it as an empty string
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = ""

# Display the conversation history header
st.write("### Chat History")

# Display the conversation history in a text area (non-editable)
st.text_area("Chat History", st.session_state['conversation'], height=200, disabled=True)

# Input box for the user to type their message
user_message = st.text_input("Your message", "")

# When the user submits a message, process and generate the chatbot's response
if user_message:
    # Update the conversation history with the user's message
    st.session_state['conversation'] += f"User: {user_message}\n"
    
    # Generate the chatbot's response using the pipeline
    response = chatbot(user_message)
    chatbot_response = response[0]['generated_text']
    
    # Update the conversation history with the chatbot's response
    st.session_state['conversation'] += f"Bot: {chatbot_response}\n"
    
    # Display the chatbot's response
    st.write(f"**Bot:** {chatbot_response}")
