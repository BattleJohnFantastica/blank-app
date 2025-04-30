import streamlit as st
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.title("PDF Page Remover")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    # Example: remove page 2 (index 1)
    for i in range(len(reader.pages)):
        if i != 1:
            writer.add_page(reader.pages[i])

    # Save to BytesIO object
    output_buffer = BytesIO()
    writer.write(output_buffer)
    output_buffer.seek(0)

    # Prompt user to download
    st.download_button(
        label="Download Edited PDF",
        data=output_buffer,
        file_name="edited.pdf",
        mime="application/pdf"
    )