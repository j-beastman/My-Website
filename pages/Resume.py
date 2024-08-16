import base64
import streamlit as st

st.set_page_config(page_title="John Eastman", page_icon="📄", layout="wide")

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1400" height="900" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

displayPDF("./static/Eastman_Resume.pdf")