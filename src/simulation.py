from image_processing import image_to_latex
from tutor import tutor_session

# Sample image path (replace with actual image)
image_path = "data/sample_math_problem.png"

# Step 1: Convert image to LaTeX
latex_problem = image_to_latex(image_path)
print(f"Extracted LaTeX: {latex_problem}")

# Step 2: Simulate tutoring session
response = tutor_session(latex_problem)
print(f"AI Tutor Response: {response}")

