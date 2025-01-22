import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OpenAI API key not found. Check your .env file.")
    exit()

# Set up the OpenAI client with the API key
client = openai.Client(api_key=api_key)

# Test the API with a basic prompt
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful math professor."},
            {"role": "user", "content": "What is the derivative of x^2?"}
        ]
    )
    print("AI Response:", response.choices[0].message.content.strip())
except Exception as e:
    print("Error:", e)
