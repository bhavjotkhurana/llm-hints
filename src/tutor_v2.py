# tutor_v2.py (migrated version)

import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Pass the API key explicitly to the client.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def tutor_session_v2(image_path):
    """
    Single-step approach using GPT-4. 
    We feed the math problem image directly to GPT-4 and request a solution.
    """
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    system_prompt = (
        "You are an SAT math tutor that can read images. "
        "Provide a step-by-step solution to the math problem in the uploaded image. "
        "Always wrap math expressions in LaTeX delimiters for Markdown rendering. "
        "For inline math use $...$, and for display math use $$...$$."
    )

    user_message = [
        {"type": "text", "text": "Please solve the problem in this image step by step."},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
    ]

    # Now call client.chat.completions.create instead of openai.ChatCompletion.create
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message.content.strip()
