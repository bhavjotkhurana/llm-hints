import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def tutor_session(latex_problem):
    """Simulate tutoring session with step-by-step hints."""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an SAT math tutor that provides hints progressively."},
            {"role": "user", "content": f"Help me solve this problem step by step: {latex_problem}."},
            {"role": "assistant", "content": "Let's start by isolating the variable."}
        ]
    )
    return response.choices[0].message.content.strip()

