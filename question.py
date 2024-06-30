import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

image_path = "test_files/test.PNG"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["日本の首都はどこですか？"])
print(response.text)
