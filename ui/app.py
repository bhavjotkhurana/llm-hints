import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.image_processing import image_to_latex
from src.tutor import tutor_session

import streamlit as st

st.title("AI SAT Math Tutor")

uploaded_file = st.file_uploader("Upload a math problem image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Processing image...")
    latex_problem = image_to_latex("temp_image.png")
    st.write("Extracted LaTeX:", latex_problem)

    if st.button("Get Tutoring Help"):
        response = tutor_session(latex_problem)
        st.write("AI Tutor Response:", response)
