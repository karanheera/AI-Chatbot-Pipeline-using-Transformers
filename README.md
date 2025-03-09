# AI Chatbot Pipeline using Transformers

## Description

This app implements a simple **AI Chatbot** using the Meta **BlenderBot** model from Hugging Face's **Transformers** library. The chatbot is built with **Streamlit** to provide an interactive web interface where users can chat with the model. The chatbot responds to user inputs with relevant responses based on the pre-trained BlenderBot model, which is capable of understanding and generating human-like conversations.

### Key Features:
- **AI Chatbot**: Chat with the AI powered by Hugging Face's facebook BlenderBot model.
- **Interactive Interface**: Built with Streamlit to allow users to interact with the chatbot.
- **Conversation History**: Keeps a log of the conversation, displaying both user inputs and chatbot responses in a continuous dialogue.
- **Simple and User-Friendly**: Just input your message and receive instant responses.

## Demo

You can try the chatbot app by visiting the app interface, typing your message, and receiving responses from the BlenderBot. The app stores the conversation history and continuously updates with each user input and chatbot response.

## Technologies Used

- **Streamlit**: To build the interactive web interface.
- **Hugging Face Transformers**: For utilizing the pre-trained Meta **BlenderBot** model.
- **Python**: The main programming language used for implementing the chatbot pipeline.

## Installation

### Prerequisites

Ensure you have **Python** installed on your system. The required Python packages are listed in the `requirements.txt` file.

1. Clone the repository:
   ```bash
   git clone https://github.com/karanheera/AI-Chatbot-Pipeline-using-Transformers.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AI-Chatbot-Pipeline-using-Transformers
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the app locally, use the following command:
```bash
streamlit run app.py
```

Once the command is executed, the Streamlit app will start running on your local server, usually at [http://localhost:8501](http://localhost:8501).

## File Structure

```plaintext
/AI-Chatbot-Pipeline-using-Transformers
│
├── app.py              # Main app file that runs the Gradio interface and story generation logic.
├── CODE_OF_CONDUCT.md  # Code of conduct file.
├── CONTRIBUTING.md     # Contribution guidelines.
├── LICENSE             # MIT License file.
├── README.md           # This file.
├── requirements.txt    # List of required Python libraries.
```

## Usage

### Start Chatting
1. Open the app in your browser.
2. Type a message in the input box and press enter.
3. The chatbot will respond with a relevant reply based on your input.
4. The conversation history will be updated with your message and the bot's response.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project was developed using the following technologies:

- **BlenderBot** from facebook on Hugging Face’s **Transformers** library. This model is used for generating chatbot responses.
- **Streamlit**: A Python library that allows for easy creation of interactive web applications.
- **Hugging Face Transformers**: A powerful library for state-of-the-art NLP models.
- Special thanks to **DeepLearning.AI** for their amazing resources, and **Hugging Face** for providing cutting-edge transformer models.

## Contributing

Contributions are welcome! If you would like to add new features or fix bugs, feel free to open an issue or submit a pull request.

Steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your forked repository.
4. Open a pull request with a clear explanation of your changes.

## Contact

For any questions or inquiries, feel free to contact the project maintainer:

**Karan Heera**  
- LinkedIn: [https://www.linkedin.com/in/karanheera/](https://www.linkedin.com/in/karanheera/)  
- GitHub: [https://github.com/karanheera](https://github.com/karanheera)
