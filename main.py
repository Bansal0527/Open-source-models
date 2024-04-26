import requests
import io
from PIL import Image
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("HUGGING_FACE_API")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# You can access the image with PIL.Image for example


image_bytes = query({
	"inputs": "Make a video thumbnail for me, video is about a cricket tournament.",
})
image = Image.open(io.BytesIO(image_bytes))
image.show()


