import streamlit as st
import pathlib as Path
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

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


sytem_prompt = """
You are designing an AI model that assists doctors and medical professionals by analyzing medical images and providing diagnostic insights.

The model’s responsibilities include the following:
1.	Image Classification:	Analyze and classify medical images (e.g., X-rays, MRIs, CT scans, ultrasounds) to identify specific categories such as normal, abnormal, or indicative of a particular condition (e.g., tumor, fracture, infection).
2.	Segmentation:Segment relevant anatomical regions (e.g., organs, tissues, or lesions) from medical images, highlighting critical areas that may require further examination.
3.	Anomaly Detection:	Detect anomalies or abnormalities in images, such as the presence of tumors, fractures, blockages, or any other pathology. The model should flag areas of concern for further review by the doctor.
4.	Feature Extraction:	Identify key features and measurements (e.g., size, shape, density) that can help in diagnosing a condition or evaluating disease progression.
5.	Diagnostic Suggestions:	Based on the analysis, provide possible diagnostic suggestions or a list of differential diagnoses for consideration by the doctor. These should be supported by the visual features extracted from the image.
Sope of response:
1.	Accuracy and Relevance:	The AI must provide responses that are directly related to the medical image being analyzed, focusing on relevant features or findings. It should not generate extraneous information outside the context of the image and its medical application.
2.	Response Clarity:	The model should deliver responses in clear, precise medical language understandable to a doctor. When addressing non-expert users, it should offer simplified explanations, using layman’s terms without compromising accuracy.
3.	Diagnostic Limitations:The AI model’s responses should include a disclaimer that its analysis is a support tool, not a definitive diagnosis. It should avoid suggesting definitive medical diagnoses without human oversight and always recommend confirmation through further clinical evaluation.
"""
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
uploaded_files = st.file_uploader("Upload your Images for Analysis", type=["png","jpg","jpeg"])

submit_button = st.button("Generate Analysis")

if submit_button:
    
    
    image_data = uploaded_files.getvalue()

    image_parts = [
        {
            "mime_type" : "image/jpeg",
            "data" : image_data
        }
    ]

    prompt_parts = [
        
        image_parts[0],
        sytem_prompt,
    ]

    chat_session = model.start_chat(
        
        history=[
        ]
    )

    response = chat_session.send_message(prompt_parts)

    #print(response.text)
    st.write(response.text)


