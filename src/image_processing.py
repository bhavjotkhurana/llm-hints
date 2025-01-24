import openai
import os
import base64
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def image_to_latex(image_path):
    """Convert a math problem image to LaTeX."""
    with open(image_path, "rb") as img:
        base64_image = base64.b64encode(img.read()).decode("utf-8")

    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Convert the image to LaTeX."},
            {"role": "user", "content": [
                {"type": "text", "text": "Convert this math problem to LaTeX format."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
            ]}
        ]
    )

    return response.choices[0].message.content.strip()
