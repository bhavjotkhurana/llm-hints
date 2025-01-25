import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.tutor_v2 import tutor_session_v2

st.title("AI SAT Math Tutor (GPT-4 Single-Step)")

# File uploader for the math problem image
uploaded_file = st.file_uploader("Upload a math problem image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Save the uploaded image to a temp file
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Processing image with GPT-4...")

    # Directly solve the problem
    response = tutor_session_v2("temp_image.png")

    st.write("### AI Tutor Response:")
    # Ensure LaTeX equations are displayed properly in Streamlit
    st.markdown(response)
else:
    st.write("Please upload an image to get started.")

st.markdown("---")
st.markdown(
    "This app uses GPT-4 (with image support) to read the uploaded math problem directly, "
    "and provide a step-by-step solution in a single step."
)
