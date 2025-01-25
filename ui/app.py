import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.image_processing import image_to_latex  # uses GPT-4 for OCR -> LaTeX
from src.tutor import initialize_conversation_v1, request_hint_v1

st.title("AI SAT Math Tutor (v1: GPT-4 -> LaTeX, then GPT-3.5 for tutoring)")

# Session state for conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "current_hint" not in st.session_state:
    st.session_state.current_hint = 0  # 0 => no hint, 1 => first hint, etc.

uploaded_file = st.file_uploader("Upload a math problem image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert image to LaTeX first
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("### Step 1: Converting image to LaTeX with GPT-4...")
    latex_problem = image_to_latex("temp_image.png")

    st.write("#### Extracted LaTeX:")
    st.write(latex_problem)

    # Button to initialize multi-hint tutoring
    if st.button("Initialize Tutor"):
        st.session_state.conversation = initialize_conversation_v1(latex_problem)
        st.session_state.current_hint = 0
        st.write("Tutor is ready. Press 'Get  Hint' to proceed.")

# Show the "Get Hint" button only if conversation is initialized
if st.session_state.conversation is not None:
    if st.button("Get Hint"):
        st.session_state.current_hint += 1

        # If the user tries for more than 3 hints, clamp at 3
        if st.session_state.current_hint > 3:
            st.session_state.current_hint = 3
            st.warning("You already received all 3 hints (including the final solution).")
        else:
            hint_text = request_hint_v1(st.session_state.conversation, st.session_state.current_hint)
            st.write(f"### Hint {st.session_state.current_hint}")
            st.markdown(hint_text)

# Optionally remove any debugging section that prints all conversation messages
# ...
