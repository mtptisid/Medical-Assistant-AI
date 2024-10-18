# Medical Assistance Chatbot

This project is a web application that utilizes Google Generative AI to assist medical professionals by analyzing medical images and providing diagnostic insights. The application allows users to upload images and receive analytical feedback through a chat interface.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload and analyze medical images (PNG, JPG, JPEG).
- Generate diagnostic insights using AI.
- Maintain a chat history for user interactions.
- Sidebar for quick access to previous chats.
- Image preview functionality.
- User-friendly input interface with a text field and send button.
- Persistent chat history that survives page refreshes.

## Technologies Used

- **Streamlit**: For building the web interface.
- **Google Generative AI**: For analyzing medical images and providing insights.
- **Python**: The programming language used for backend logic.
- **JSON**: For storing chat history persistently.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mtptisid/Medical-Assistant-AI.git
   cd Medical-Assistant-AI
   ```

2. **Install Dependencies**

   Make sure you have Python installed. Then install the required packages using pip:

   ```bash
   pip install streamlit google-generativeai
   ```

3. **Set Up API Key**

   Create a file named `api_key.py` in the root directory and add your Google Generative AI API key:

   ```python
   api_key = "your_api_key_here"
   ```

4. **Run the Application**

   Start the Streamlit application by running:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of your main Python file if different.

## Usage

1. Open the application in your web browser (usually at `http://localhost:8501`).
2. Upload a medical image using the file uploader.
3. Optionally, provide additional context in the text input field.
4. Click the send icon (📤) to generate analysis.
5. View the chat history on the sidebar for previous interactions.

## File Structure

```
/your-project-directory
│
├── app.py               # Main application file
├── api_key.py           # API key configuration
├── chat_history.json     # Persistent chat history storage
├── ai_healthcare.jpeg.webp  # Sample image for display
└── requirements.txt      # List of dependencies (optional)
```

## Screenshots :
...

<img width="1440" alt="Screenshot 2024-09-22 at 2 02 24 PM" src="https://github.com/user-attachments/assets/ccc6bd92-55ff-4729-b415-1fdff4daf163">


<img width="1440" alt="Screenshot 2024-09-22 at 2 01 29 PM" src="https://github.com/user-attachments/assets/130f22fc-3570-4ea8-8e41-14b8e9073d24">


## Videos :



https://github.com/user-attachments/assets/e25850e0-ca8b-44b4-b39e-e11f61db1f1a




## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
