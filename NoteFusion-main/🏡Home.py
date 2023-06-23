import requests
import streamlit as st
from PIL import Image
from poppler_installer import download_and_install_poppler
import pathlib
from streamlit_extras.switch_page_button import switch_page
import logging
from bs4 import BeautifulSoup
import shutil
# from streamlit_ga import ga_track_page

# ga_tracking_id = 'G-9K8R57LTJC'  # Replace with your actual tracking ID
# ga_track_page(ga_tracking_id, 'Home')
st.set_page_config(page_title="MyClassroom", page_icon="📝", layout="wide",initial_sidebar_state="collapsed")

def inject_ga():
    GA_ID = "google_analytics"


    GA_JS = """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-9K8R57LTJC"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-9K8R57LTJC');
    </script>
    """

    # Insert the script in the head tag of the static template inside your virtual
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'editing {index_path}')
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID): 
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  
        else:
            shutil.copy(index_path, bck_index)  
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_JS)
        index_path.write_text(new_html)


inject_ga()
#streamlit run 🏡Home.py
url = 'https://api.pawan.krd/resetip'
headers = {
    'Authorization': 'Bearer (api key)'
}

response1 = requests.post(url, headers=headers)
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
download_and_install_poppler()





imagef = Image.open('logo.png')
pdf_img=Image.open('pdf_doc.png')
pic=Image.open('picture.png')
bot=Image.open("bot.png")
res_bot=bot.resize((250,250))
resiz_pic=pic.resize((250, 250))

# Resize the image
resized_image = pdf_img.resize((250, 250))

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:

        st.title("NoteFusion")
        st.write(
            "Streamline Your Learning with AI"
        )
        st.write("---")
        st.subheader(
            """
            Our AI copilot is a powerful learning tool that helps students understand and summarize their notes.
            By leveraging cutting-edge technologies like natural language processing and machine learning,
             our copilot can identify important concepts, provide detailed explanations, and generate concise summaries
             of complex texts. With our AI copilot, students can streamline their learning process and improve their
             comprehension, making studying more efficient and effective.
            """
        )
        st.subheader("Get started with:")



    with right_column:
        st.image(imagef, use_column_width=True)
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image(resized_image, use_column_width=False)
        with right_column:

            st.subheader(
                "Adding PDFs and Getting Summaries: Our platform lets you easily upload and manage your PDFs. With just a few clicks, you can get concise summaries of your documents, making it easy to quickly review and understand key concepts.")
            st.write("Try it now:")
            want_to_contribute1 = st.button("📁PDF")
            if want_to_contribute1:
                switch_page("pdf")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader(
                "Image Text Extraction: We use advanced OCR technology to extract text from images, making it easy to add image-based content to your study materials. Say goodbye to manual typing and hello to more efficient learning.")

            st.write("Try it now:")
            want_to_contribute2 = st.button("📷Image")
            if want_to_contribute2:
                switch_page("image")

        with right_column:
            st.image(resiz_pic, use_column_width=False)
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image(res_bot, use_column_width=False)
        with right_column:

            st.subheader(
                "Doubtbot: Our Doubtbot feature provides instant answers to your questions, allowing you to get the help you need right when you need it. With our AI-powered chatbot, you can get quick and accurate answers related to your study materials, saving you time and effort.")
            st.write("Try it now:")
            want_to_contribute3 = st.button("🤖 DoubtBot")
            if want_to_contribute3:
                switch_page("doubtbot")

