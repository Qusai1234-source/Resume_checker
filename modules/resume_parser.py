from pypdf import PdfReader


def extract_text_pdf(resume_path):
    with open(resume_path, "rb") as file:
        reader = PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

