import os

import google.generativeai as genai
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

pdf_path = "test_files/test.pdf"

reader = PdfReader(pdf_path)
number_of_pages = len(reader.pages)
text = ""
for i in range(number_of_pages):
    text += reader.pages[i].extract_text()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["次の文章を要約して\n", text])
print(response.text)
