import pdfplumber
import openai
import PyPDF2
file = open('PPS Notes Unit-I.pdf', 'rb')
readpdf = PyPDF2.PdfReader(file)
totalpages = len(readpdf.pages)
for i in range(totalpages):
    with pdfplumber.open("PPS Notes Unit-I.pdf") as pdf:
        first_page = pdf.pages[i]
        x = first_page.extract_text()
    openai.api_key = 'pk-fVBWioLIbzTFlKlKokaWGFRXGdKrLWCrovPTNHVMqEKtuVZn'
    openai.api_base  = 'https://api.pawan.krd/v1'

    prop= x+  "These are the contents of a single page of a pdf.Identify the all topics and subtopics covered in this page using NLP techniques such as Named Entity Recognition and Topic Modeling. Generate a summary of the page by selecting the most important sentences and phrases related to the identified topics and subtopics. Create a concise summary of the page based on the selected sentences and phrases. The summary should be roughly based on all the contents of the page. Return the summary of the page as output."

    response = openai.Completion.create(

        model="gpt-3.5-turbo",
        prompt=prop,
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
    print (response.choices[0].text)
    x=""

totalpages = len(readpdf.pages)
for i in range(totalpages):
    with pdfplumber.open("PPS Notes Unit-I.pdf") as pdf:
        first_page = pdf.pages[i]
        x = first_page.extract_text()
    openai.api_key = 'pk-fVBWioLIbzTFlKlKokaWGFRXGdKrLWCrovPTNHVMqEKtuVZn'
    openai.api_base  = 'https://api.pawan.krd/v1'

    prop= x+  "These are the contents of a single page of a pdf.Identify the all topics and subtopics covered in this page using NLP techniques such as Named Entity Recognition and Topic Modeling. Generate a summary of the page by selecting the most important sentences and phrases related to the identified topics and subtopics. Create a concise summary of the page based on the selected sentences and phrases. The summary should be roughly based on all the contents of the page. Return the summary of the page as output."

    response = openai.Completion.create(

        model="gpt-3.5-turbo",
        prompt=prop,
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
    print (response.choices[0].text)
    x=""

