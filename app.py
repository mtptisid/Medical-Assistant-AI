import streamlit as st
import pathlib as Path
import google.generativeai as genai

#import keys
from api_key import api_key

#configure genai module
genai.configure(api_key=api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 4096,
  "response_mime_type": "text/plain",
}
#model configuration

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
   safety_settings = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

st.set_page_config(page_title="Medical Assistance", page_icon=":robot:")

st.image("ai_healthcare.jpeg.webp", width=100)

st.title("The Medical 🏥 Assistance 🤖")

st.subheader("Complete assistance for an Medical  🏥 related issues by Image")
uploaded_images = st.file_uploader("Upload your Images for Analysis", type=["png","jpg","jpeg"])

submit_button = st.button("Generate Analysis")
