import openai
import os
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Check your .env file.")

# Path to your image file
image_path = "/Users/bhavjotsingh/Desktop/test-question.png"

def analyze_image(image_path):
    try:
        # Convert image to Base64 encoding
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        # Properly structure the request to GPT-4 Turbo Vision API for LaTeX conversion
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in converting math images to LaTeX."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Convert this math problem to LaTeX format, no need to solve the question. If LaTeX is not available, like for a graph, try your best to describe the graph."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                    ]
                }
            ],
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"

# Run the function and print the result
result = analyze_image(image_path)
print("AI Response:\n", result)
