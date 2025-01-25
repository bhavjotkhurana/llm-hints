import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def initialize_conversation(image_path):
    """
    Sets up the initial conversation with GPT-4 to 'read' the problem from the image.
    Returns a list of messages that can be stored in session state.
    """
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    # The system prompt: how GPT-4 should behave.
    system_prompt = (
        "You are an SAT math tutor that can read images. "
        "You'll provide up to 3 hints total. The third hint must include the full solution. "
        "Wait for the user to request each hint explicitly. "
        "Wrap math expressions in LaTeX delimiters. "
        "For inline math use $...$, and for display math use $$...$$."
    )

    # First user message: "Here's the problem"
    user_message = [
        {"type": "text", "text": "Here is the problem. I will ask for hints one by one."},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
    ]

    # The conversation so far
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    # GPT-4's first reply: acknowledges the problem
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )

    # Add GPT-4’s reply to the conversation
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

    return messages

def request_hint(conversation, hint_number):
    """
    Asks GPT-4 for the next hint.
    `conversation` is the list of messages so far.
    `hint_number` is which hint the user is requesting (1, 2, or 3).
    The third hint includes the full solution.
    """
    user_prompt = f"Please give me hint #{hint_number}."
    conversation.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=conversation
    )

    assistant_reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": assistant_reply})

    # Return the assistant's new hint (but also store it in conversation)
    return assistant_reply
