import os

import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv

load_dotenv()

# image_path = "test_files/test.PNG"
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# img = PIL.Image.open(image_path)
# model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# response = model.generate_content(["What is in this photo?", img])
# print(response.text)

image_path = "test_files/car.jpg"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
img = PIL.Image.open(image_path)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(
    [
        "List the areas of the image that need to be kept private for segmentation. Just respond with area names, e.g., \"'face', 'license plate'\".",
        img,
    ]
)
print(response.text)
