import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.tutor_v2 import initialize_conversation, request_hint

st.title("SAT Math Tutor (GPT-4 Step-by-Step Hints)")

# Keep track of conversation and which hint the student is on
if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "current_hint" not in st.session_state:
    st.session_state.current_hint = 0  # 0 means no hint yet, 1 => first hint, etc.

# File uploader for the math problem image
uploaded_file = st.file_uploader("Upload a math problem image", type=["png", "jpg", "jpeg"])

# Button to initialize conversation
if uploaded_file is not None and st.button("Initialize Tutor"):
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.conversation = initialize_conversation("temp_image.png")
    st.session_state.current_hint = 0
    st.write("Tutor is ready. Click 'Get Hint' to proceed.")

# Button to request next hint
if st.session_state.conversation is not None:
    if st.button("Get Hint"):
        st.session_state.current_hint += 1

        # If the user tries to get more than 3 hints, cap it at 3 (the third includes the solution)
        if st.session_state.current_hint > 3:
            st.session_state.current_hint = 3  # no more than 3
            st.warning("You have already received the full solution.")
        else:
            hint_text = request_hint(
                st.session_state.conversation,
                st.session_state.current_hint
            )
            st.write(f"### Hint #{st.session_state.current_hint}")
            st.markdown(hint_text)

# Display the conversation so far (optional)
# if st.session_state.conversation:
#     st.markdown("---")
#     st.subheader("Conversation so far (for debugging):")

#     for i, msg in enumerate(st.session_state.conversation):
#         role = msg["role"]
#         content = msg["content"]

#         # If this is the user message with the image, let's shorten or skip it
#         if role == "user" and isinstance(content, list):
#             # Check if there's an image element in the list
#             has_image = any(
#                 (
#                     ("type" in part and part["type"] == "image_url")
#                     or ("image_url" in part)
#                 )
#                 for part in content
#             )
#             if has_image:
#                 st.write("**User**: [Image data hidden for brevity]")
#                 continue  # Skip printing the raw content

#         # If we didn't skip, print normally
#         st.write(f"**{role.capitalize()}**: {content}")

