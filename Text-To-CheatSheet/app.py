import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
import markdown
from xhtml2pdf import pisa
import io

# --- CONFIGURATION ---
st.set_page_config(page_title="Notes-to-Cheatsheet Generator", layout="wide")

# --- AUTHENTICATION LOGIC ---
api_key = st.secrets.get("GOOGLE_API_KEY", None)

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Settings")
    if not api_key:
        api_key = st.text_input("Enter Gemini API Key", type="password")
    
    style = st.selectbox(
        "Cheatsheet Style",
        ("Standard", "Code-Heavy", "Academic/Exam Prep", "ELI5 (Explain like I'm 5)")
    )

# --- FUNCTIONS ---

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def convert_markdown_to_pdf(markdown_content):
    """
    Converts Markdown text to a PDF byte string.
    1. Markdown -> HTML
    2. HTML -> PDF
    """
    # Convert Markdown to HTML (enable tables extension)
    html_text = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code'])
    
    # Add CSS for styling (Make it look like a real document)
    styled_html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Helvetica, sans-serif; font-size: 12pt; }}
            h1 {{ color: #2E86C1; border-bottom: 2px solid #2E86C1; }}
            h2 {{ color: #1B4F72; margin-top: 20px; }}
            h3 {{ color: #1B4F72; }}
            code {{ background-color: #f4f4f4; padding: 2px; border-radius: 3px; font-family: Courier; }}
            pre {{ background-color: #f4f4f4; padding: 10px; border: 1px solid #ddd; }}
            table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        {html_text}
    </body>
    </html>
    """
    
    # Generate PDF
    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(styled_html, dest=pdf_buffer)
    
    if pisa_status.err:
        return None
    return pdf_buffer.getvalue()

def generate_cheatsheet(text, style_preference, key):
    try:
        genai.configure(api_key=key)
        # UPDATED MODEL NAME BASED ON YOUR LIST
        model = genai.GenerativeModel('models/gemini-2.5-flash') 
        
        prompt = f"""
        You are an expert technical writer. Convert these notes into a concise cheatsheet.
        Style: {style_preference}
        Format: Markdown, Tables, Bullet points, Bold key terms. 
        Important: Do not start with "Here is a cheatsheet". Just give the content.
        Notes: {text}
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# --- MAIN UI ---
st.title("📝 Notes ➡️ Cheatsheet")

tab1, tab2 = st.tabs(["📂 Upload File", "✍️ Paste Text"])
input_text = ""

with tab1:
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file:
        input_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF Loaded!")

with tab2:
    pasted_text = st.text_area("Paste notes here", height=200)
    if pasted_text:
        input_text = pasted_text

if st.button("Generate Cheatsheet 🚀", type="primary"):
    if not api_key:
        st.error("❌ No API Key found.")
    elif not input_text:
        st.warning("Please provide some text to analyze.")
    else:
        with st.spinner("Processing with Gemini 2.5..."):
            # 1. Generate Content
            markdown_result = generate_cheatsheet(input_text, style, api_key)
            st.session_state['generated_result'] = markdown_result # Save to state so it persists
            
            # 2. Display Result
            st.divider()
            st.markdown(markdown_result)

# --- DOWNLOAD SECTION ---
# We check if result exists in session_state so the button stays visible
if 'generated_result' in st.session_state:
    st.divider()
    st.subheader("📥 Download")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Download as Markdown
        st.download_button(
            label="Download Source (.md)",
            data=st.session_state['generated_result'],
            file_name="cheatsheet.md",
            mime="text/markdown"
        )
        
    with col2:
        # Download as PDF
        pdf_bytes = convert_markdown_to_pdf(st.session_state['generated_result'])
        if pdf_bytes:
            st.download_button(
                label="Download PDF (.pdf)",
                data=pdf_bytes,
                file_name="cheatsheet.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Error creating PDF.")