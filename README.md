##🧠 Adobe India Hackathon 2025 – Round 1A & Round 1B
This repository contains the solutions for Adobe India Hackathon 2025:

✅ Round 1A – Intelligent Document Classification

✅ Round 1B – Context-Aware Document Understanding using Persona

📂 Folder Structure
bash
Copy
Edit
.
├── challenge1a/       # Solution for Challenge 1A
├── round1b/           # Solution for Round 1B
├── .gitignore
🧩 Round 1A – Document Classification
🔍 Problem Statement
Build an intelligent system that classifies documents (e.g. invoices, resumes, articles) into predefined categories using semantic and structural understanding.

⚙ Tech Stack
Language: Python

Framework: Scikit-learn, Pandas

Model: Classical ML & Rule-based classifiers

🚀 How to Run
bash
Copy
Edit
cd challenge1a
python classify.py  # or your main script
🧠 Round 1B – Persona-based Document Analysis
🔍 Problem Statement
Create a system that reads multiple documents and summarizes relevant insights based on a specific user's persona.

⚙ Tech Stack
Language: Python

Framework: Flask, OpenAI API, PyMuPDF

Execution: Dockerized

🧪 Folder Structure
graphql
Copy
Edit
round1b/
├── input/            # PDF documents and persona.json
├── output/           # Output summaries
├── src/
│   ├── app.py        # Flask API
│   └── utils.py      # Core logic
├── requirements.txt
└── Dockerfile
🚀 How to Run (with Docker)
bash
Copy
Edit
cd round1b
docker build -t round1b .
docker run --rm -v "%cd%\input:/app/input" -v "%cd%\output:/app/output" -p 5000:5000 round1b
Then go to: http://127.0.0.1:5000/analyze

🙌 Team Members
Rupesh Dahale (Team Leader)
Vedant Yengul
