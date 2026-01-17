# 📝 Notes-to-Cheatsheet Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Gemini AI](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-8E75B2)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Turn weeks of study material into a single page in seconds.**

The **Notes-to-Cheatsheet Generator** is a streamlined web application powered by **Google's Gemini 2.5 Flash model**. It ingests lengthy lecture notes, technical documentation, or PDF files and transforms them into concise, high-utility cheatsheets tailored to your specific study needs.

---

## 🚀 Features

* **📄 PDF & Text Support:** Upload PDF files directly or paste raw text from your notes.
* **🧠 Advanced AI:** Powered by `gemini-2.5-flash` for high-speed, high-accuracy summarization.
* **🎨 Custom Styles:** Choose from multiple output styles (*Standard, Code-Heavy, Academic, ELI5*).
* **📥 Export Ready:** Download your cheatsheets as editable **Markdown (.md)** or professional **PDF (.pdf)**.
* **🔒 Secure:** Uses `secrets.toml` to safely handle API keys.

---

## 🛠 Tech Stack

* **Frontend/Backend:** [Streamlit](https://streamlit.io/)
* **AI Model:** [Google Gemini API](https://ai.google.dev/) (`google-generativeai`)
* **PDF Processing:** `pypdf` (reading), `xhtml2pdf` (writing)
* **Formatting:** `markdown` library

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/notes-to-cheatsheet.git](https://github.com/yourusername/notes-to-cheatsheet.git)
cd notes-to-cheatsheet
```
2️⃣ Set Up a Virtual Environment (Recommended)
🪟 Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate

🐧 macOS / Linux (Bash)
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
Using requirements.txt (Recommended)
pip install -r requirements.txt

If requirements.txt is not created yet
pip install streamlit google-generativeai pypdf markdown xhtml2pdf

🔑 Gemini API Configuration

You must obtain a Google Gemini API key.

👉 Get your API key from:
https://aistudio.google.com/app/apikey

🔐 Option 1: Secure Method (Recommended)

Keeps your API key out of version control.

Step 1: Create .streamlit directory
.streamlit/

Step 2: Create secrets.toml
.streamlit/secrets.toml

Step 3: Add your API key
GOOGLE_API_KEY = "AIzaSyD-Your-Actual-Key-Here"


✅ This file should be gitignored.

✍️ Option 2: Manual API Key Entry

If no secrets.toml file is found:

The app will show a sidebar input field

Paste your Gemini API key each time you run the app

⚠️ Less secure, but useful for quick testing.

▶️ Usage
Launch the App
streamlit run app.py

Access the Interface

The app opens automatically at:

http://localhost:8501

Generate a Cheatsheet

📄 Upload a PDF file OR paste raw text

🎨 Choose a style (Academic / Code-Heavy)

🚀 Click Generate Cheatsheet

📥 Download as PDF or Markdown

📂 Project Structure
notes-to-cheatsheet/
├── .streamlit/
│   └── secrets.toml        # API credentials (gitignored)
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

git checkout -b feature/NewFeature


Commit your changes

Push to your fork

Open a Pull Request

📜 License

This project is intended for educational and personal use.
You are free to modify and extend it.

⭐ Acknowledgements

Google Gemini AI

Streamlit Community

Open-source contributors

Happy studying 📚🚀


---

If you want next:
- `requirements.txt`
- `app.py` (Streamlit Gemini app)
- Project abstract
- Viva questions & answers

Just tell me 👌
