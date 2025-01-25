import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables, e.g. your OPENAI_API_KEY
load_dotenv()

# Create an OpenAI client (assuming you have 'openai>=1.0.0')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def tutor_session(latex_problem):
    """
    Original single-shot tutoring function (v1).
    Uses GPT-3.5-Turbo to provide step-by-step hints in one go.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an SAT math tutor that provides hints progressively. "
                    "Always wrap your math expressions in LaTeX delimiters so that "
                    "they can be rendered by Markdown. For inline math use $...$, "
                    "and for display math use $$...$$. Provide step-by-step explanations."
                )
            },
            {
                "role": "user",
                "content": f"Help me solve this problem step by step: {latex_problem}"
            },
            {
                "role": "assistant",
                "content": "Let's start by isolating the variable."
            }
        ]
    )
    return response.choices[0].message.content.strip()


def initialize_conversation_v1(latex_problem):
    """
    Sets up the initial conversation with GPT-3.5 for a multi-hint approach,
    using the LaTeX problem from image_to_latex().
    GPT-3.5 will only reveal one hint at a time, up to 3 hints total.
    The third hint includes the full solution.
    """
    system_prompt = (
        "You are an SAT math tutor. You have the following LaTeX problem:\n"
        f"{latex_problem}\n\n"
        "You will provide up to 3 hints total. The third hint must include the full solution. "
        "Wait for the user to explicitly request each hint. "
        "Always wrap math expressions in LaTeX delimiters for Markdown rendering. "
        "Please do not use \begin{align*} or other LaTeX environments. Use $$ ... $$ for any multi-line math or keep it inline with $ ... $."
    )

    # Begin the conversation
    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": (
                "I have a math problem in LaTeX format above. "
                "I will ask you for hints one at a time."
            ),
        },
    ]

    # GPT-3.5's first response acknowledging the problem
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response.choices[0].message.content

    # Add GPT-3.5's response to the conversation
    messages.append({"role": "assistant", "content": assistant_reply})

    return messages


def request_hint_v1(conversation, hint_number):
    """
    Asks GPT-3.5 for the next hint for the LaTeX problem.
    `conversation`: list of messages so far
    `hint_number`:  which hint (1, 2, or 3)
    The third hint must reveal the final solution.
    """
    # User explicitly requests hint n
    user_prompt = f"Please give me hint #{hint_number}."
    conversation.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    assistant_reply = response.choices[0].message.content

    # Append GPT-3.5's reply to the conversation
    conversation.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply
