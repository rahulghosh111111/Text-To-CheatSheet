# 📝 Notes-to-Cheatsheet Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Gemini AI](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-8E75B2)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Streamlit-based web application that leverages **Google's Gemini 2.5 Flash model** to convert lengthy lecture notes, PDFs, and technical documentation into concise, study-ready cheatsheets.

**Turn weeks of study material into a single page in seconds.**

---

## 🚀 Features

* **📄 PDF & Text Support:** Upload PDF files directly or paste raw text from your notes.
* **🧠 Advanced AI:** Powered by `gemini-2.5-flash` for high-speed, high-accuracy summarization and context understanding.
* **🎨 Custom Styles:** Choose the perfect format for your needs:
    * *Standard:* General purpose summaries.
    * *Code-Heavy:* Optimized for developers with syntax highlighting.
    * *Academic:* Strict formatting for exam preparation.
    * *ELI5:* Simplified explanations for complex topics.
* **📥 Export Ready:** Download your cheatsheets immediately as editable **Markdown (.md)** or professional **PDF (.pdf)** files.
* **🔒 Secure:** Utilizes `secrets.toml` to safely handle API keys without hardcoding them into your script.

---

## 🛠 Tech Stack

* **Frontend/Backend:** [Streamlit](https://streamlit.io/)
* **AI Model:** [Google Gemini API](https://ai.google.dev/) (`google-generativeai`)
* **PDF Processing:** `pypdf` (reading), `xhtml2pdf` (writing)
* **Formatting:** `markdown` library

---

## ⚙️ Installation

### 1. Clone the Repository
bash
git clone [https://github.com/yourusername/notes-to-cheatsheet.git](https://github.com/yourusername/notes-to-cheatsheet.git)
cd notes-to-cheatsheet


2. Set up a Virtual Environment
It is recommended to use a virtual environment to keep dependencies clean.

Windows:

Bash

python -m venv venv
venv\Scripts\activate
Mac/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install streamlit google-generativeai pypdf markdown xhtml2pdf
🔑 Configuration (API Key)
You need a Google Gemini API key to run this project. Get one here at Google AI Studio.

Option 1: The Secure Way (Recommended)
Create a folder named .streamlit in the root directory.

Create a file inside it named secrets.toml.

Add your key to the file:

Ini, TOML

# .streamlit/secrets.toml
GOOGLE_API_KEY = "AIzaSyD-Your-Actual-Key-Here"
Option 2: The Manual Way
If you don't set up secrets.toml, the app will simply ask you to enter the key in the sidebar every time you launch the application.

▶️ Usage
Run the application using Streamlit:

Bash

streamlit run app.py
The app will open automatically in your browser at http://localhost:8501.

Select Input: Upload a PDF or paste text.

Choose Style: Select "Code-Heavy" for programming notes or "Academic" for exams.

Generate: Click the button and wait for Gemini 2.5 to process.

Download: Save the result as a PDF or Markdown file.
