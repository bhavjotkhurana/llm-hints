import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Check your .env file.")

# Create an OpenAI client using the new API syntax
client = openai.Client(api_key=api_key)

def get_math_help(question):
    """Ask the AI math tutor a question and get a solution with strategy."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an SAT math tutor providing detailed solutions and test-taking strategies."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Welcome to the AI SAT Math Tutor!")
    while True:
        question = input("Enter an SAT math question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = get_math_help(question)
        print("\nAI Tutor Response:\n", answer)
