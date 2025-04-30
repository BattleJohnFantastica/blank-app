import streamlit as st
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.title("PDF Page Remover (hello Kathleen)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    writer = PdfWriter()
    num_pages = len(reader.pages)
    st.write(f"Number of pages: {len(reader.pages)}")
    # Example: remove page 2 (index 1)
    pages_to_remove = st.multiselect(
        "Select pages to remove (1-based):",
        options=list(range(1, num_pages + 1)),
        format_func=lambda x: f"Page {x}"
    )
    for i in range(num_pages):
        if (i + 1) not in pages_to_remove:
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