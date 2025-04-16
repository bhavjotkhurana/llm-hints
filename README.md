# LLM Hints

**llm-hints** is an experimental tool that uses large language models (LLMs) to provide guided hints for SAT math problems based on image inputs. Users upload an image of a math question, and the model returns tutoring-style hints to help the student work through the problem step by step. A user can click the hint button 3 times (max) and on the 3rd press the LLM generates the entire solution with the answer. 

This project focuses on exploring how LLMs can encourage learning by avoiding direct answers and instead guiding students toward the solution.

## Features

- Upload an image of an SAT-style math problem.
- Use GPT-4 Turbo with vision capabilities to interpret the image and generate tutoring hints.
- Responses are structured to guide the student, not just give final answers.
- Lightweight Streamlit interface for testing and demonstration.

## Purpose

The goal of this project is not to deploy a production tutoring app but to simulate a learning-focused interaction and try to understand the best prompts to use give the students progressive hints that enable instead of hinder their learning abilities.

## Future Directions

- Simulate and log multiple tutoring sessions for analysis.
- Experiment with different hinting strategies (Socratic, scaffolded, etc.).
- Benchmark performance and cost against alternative approaches (e.g. OCR + cheaper models).

