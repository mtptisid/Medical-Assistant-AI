import streamlit as st
import google.generativeai as genai
import json
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from api_key import api_key

# Configure genai module
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 4096,
    "response_mime_type": "text/plain",
}

system_prompt = """
You are designing an AI model that assists doctors and medical professionals by analyzing medical images and providing diagnostic insights.

The model’s responsibilities include:
1. Image Classification: Analyze and classify medical images (e.g., X-rays, MRIs, CT scans, ultrasounds) to identify specific categories such as normal, abnormal, or indicative of a particular condition (e.g., tumor, fracture, infection).
2. Segmentation: Segment relevant anatomical regions (e.g., organs, tissues, or lesions) from medical images, highlighting critical areas that may require further examination.
3. Anomaly Detection: Detect anomalies or abnormalities in images, such as the presence of tumors, fractures, blockages, or any other pathology. The model should flag areas of concern for further review by the doctor.
4. Feature Extraction: Identify key features and measurements (e.g., size, shape, density) that can help in diagnosing a condition or evaluating disease progression.
5. Diagnostic Suggestions: Based on the analysis, provide possible diagnostic suggestions or a list of differential diagnoses for consideration by the doctor. These should be supported by the visual features extracted from the image.
"""

# Model configuration
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }
)

# Define file path for persistent storage
CHAT_FILE = "chat_history.json"

# Function to load chat history from file
def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as file:
            return json.load(file)
    return {"chat_history": [], "full_chat_history": []}

# Function to save chat history to file
def save_chat_history(chat_history, full_chat_history):
    with open(CHAT_FILE, "w") as file:
        json.dump({"chat_history": chat_history, "full_chat_history": full_chat_history}, file)

# Load chat history from file at app start
if "chat_history" not in st.session_state:
    history_data = load_chat_history()
    st.session_state["chat_history"] = history_data["chat_history"]
    st.session_state["full_chat_history"] = history_data["full_chat_history"]
    st.session_state["selected_chat"] = None  # Default to None

# Sidebar for chat session history
st.sidebar.title("Chat History")
for i, chat_summary in enumerate(st.session_state["chat_history"]):
    if st.sidebar.button(f"Chat {i+1}: {chat_summary}", key=f"button_{i}"):
        st.session_state["selected_chat"] = i

# Display header and subheader
st.image("ai_healthcare.jpeg.webp", width=100)
st.title("The Medical 🏥 Assistance 🤖")
st.subheader("Complete assistance for Medical 🏥 related issues by Image")

# Handle file uploads and preview image
uploaded_files = st.file_uploader("Upload your Images for Analysis", type=["png", "jpg", "jpeg"])
if uploaded_files:
    st.image(uploaded_files, caption="Selected Image Preview", use_column_width=True)

# Chat area: Display the selected chat if a chat is selected
if st.session_state["selected_chat"] is not None:
    selected_index = st.session_state["selected_chat"]
    st.markdown("---")  # A separator to make it cleaner
    st.write(f"**Chat {selected_index + 1}:**")
    st.write(st.session_state["full_chat_history"][selected_index])

# Spacer to ensure chat is between header and input field
st.markdown("---")

# Fixed input area at the bottom of the page
input_col1, input_col2 = st.columns([9, 1])
with input_col1:
    user_prompt = st.text_input("Enter additional context or description (optional):", key="user_input")
with input_col2:
    submit_button = st.button("📤", key="send_button")

# Process new chat if Send button is clicked and image is uploaded
if submit_button and uploaded_files is not None:
    image_data = uploaded_files.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        }
    ]

    # Combine image parts with system prompt and user input
    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]
    
    if user_prompt:
        prompt_parts.append(user_prompt)

    # Start a new chat session
    chat_session = model.start_chat(history=[])
    
    response = chat_session.send_message(prompt_parts)

    # Generate chat summary and append full chat
    summary = " ".join(response.text.split()[:10]) + "..."  # Summarize the first 10 words
    st.session_state["chat_history"].append(summary)
    st.session_state["full_chat_history"].append(response.text)

    # Save the updated chat history to file
    save_chat_history(st.session_state["chat_history"], st.session_state["full_chat_history"])

    # Immediately show the current chat
    st.markdown("---")
    st.write(f"**Current Chat Session:**")
    st.write(response.text)

# No chat is displayed by default unless a session is selected