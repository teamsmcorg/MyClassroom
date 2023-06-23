import requests
from PIL import Image
import streamlit as st
import openai
from streamlit_chat import message as st_message
from streamlit_extras.switch_page_button import switch_page
from google.cloud import vision
from google.oauth2 import service_account
credentials_path = 'api-key.json'
url = 'https://api.pawan.krd/resetip'
headers = {
    'Authorization': 'Bearer (api key)'
}

response1 = requests.post(url, headers=headers)
# Initialize the client
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = vision.ImageAnnotatorClient(credentials=credentials)

st.set_page_config(page_title="Image", page_icon="📷", layout="wide")
st.title("Upload An Image")
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# tessdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/5/tessdata/"'

img1 = st.file_uploader("Select an image 📷", type=["jpg", "jpeg", "png"])

if img1 is not None:
    #image = Image.open(img1)
    content = img1.read()

    image1 = vision.Image(content=content)  # Pass the image content as bytes

    resp = client.text_detection(image=image1)
    texts = resp.text_annotations

    if texts:
        extracted_text = texts[0].description


    # Use the OpenAI API to generate a summary of the extracted text
    openai.api_key = '(api key)'
    openai.api_base = 'https://api.pawan.krd/v1'

    prop = "These are the contents of a text generated by OCR from an image of a textbook. " \
                            "Identify all the topics and subtopics covered in this page using NLP techniques such as " \
                            "Named Entity Recognition and Topic Modeling. Generate a summary of the content by selecting " \
                            "the most important sentences and phrases related to the identified topics and subtopics. " \
                            "Create a concise summary of the page based on the selected sentences and phrases. The summary " \
                            "should be roughly based on all the contents of the page. The response must start with 'The " \
                            "summary is: .....'. towards the end add a neatly formatted list of important keywords and " \
                            "creative pneumonics to help remember them in the exam." + extracted_text

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prop,
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Display the generated summary in the Streamlit app
    st_message(response.choices[0].text)

st.write("---")
want_to_contribute = st.button("Have a Doubt 🤖 ?")
if want_to_contribute:
    switch_page("doubtbot")
