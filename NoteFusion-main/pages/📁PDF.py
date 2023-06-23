import streamlit as st
import PyPDF4
import pdfplumber
import openai
import PyPDF2
from streamlit_chat import message as st_message
import io
from google.cloud import vision
from google.oauth2 import service_account
from pdf2image import convert_from_path
import json
from pdf2image import convert_from_bytes
import os
# Upload a PDF file
credentials_path = 'api-key.json'
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = vision.ImageAnnotatorClient(credentials=credentials)

st.set_page_config(page_title="PDF", page_icon="📁", layout="wide")
st.title("Upload Your PDF")
uploaded_file = st.file_uploader("Choose a PDF file 📁", type="pdf")

# If a file was uploaded
if uploaded_file is not None:
    pdf_path=uploaded_file.read()
    images = convert_from_bytes(pdf_path)
    for i, image in enumerate(images):
        # Convert image to byte stream
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        content = img_byte_arr.getvalue()

        # Create the image object
        image = vision.Image(content=content)

        # Perform text detection on the image
        response = client.text_detection(image=image)
        texts = response.text_annotations

    # Display the extracted text
        print(f'Page {i+1}:')
        if texts:
            words = [text.description for text in texts[1:]]
            x = ' '.join(words)
            openai.api_key = 'here'
            openai.api_base = 'https://api.pawan.krd/v1'

            prop = x + "These are the contents of a single page of a pdf.Identify the all topics and subtopics covered in this page using NLP techniques such as Named Entity Recognition and Topic Modeling. Generate a summary of the page by selecting the most important sentences and phrases related to the identified topics and subtopics. The summary should be roughly based on all the contents of the page. The response must start with 'The summary of this page is: .....'."

            response = None
            while response is None:
                try:
                    response = openai.Completion.create(
                        model="gpt-3.5-turbo",
                        prompt=prop,
                        temperature=0.7,
                        max_tokens=250,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0,
                )
                    st_message(response.choices[0].text)
                    st.write("PgNo:",i+1,"----------------------------------------------------------------------------------------------------------------")
                    x = ""
                except Exception as e:
                    print(f"Error occurred: {e}")
                    print("Retrying...")
                    continue

from streamlit_extras.switch_page_button import switch_page
st.write("---")
want_to_contribute = st.button("Have a Doubt 🤖 ?")
if want_to_contribute:
    switch_page("doubtbot")

