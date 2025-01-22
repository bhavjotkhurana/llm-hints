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

        # Properly structure the request to the GPT-4 Vision API
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI SAT math tutor. Say that you can't answer any questions other than math questions if given a different topic.  Extract math problem from the image and provide a solution and test-taking strategies, simple bullet points. "
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Please analyze the attached SAT math problem and provide a solution."},
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
