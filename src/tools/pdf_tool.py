from pypdf import PdfReader

def read_pdf(path):
    reader = PdfReader(path)
    
    full_text = []
    
    for page in reader.pages:
        full_text.append(page.extract_text())
    
    return '\n'.join(full_text)

def extract_pages(path):
    reader = PdfReader(path)
    return reader.pages

def count_pages(path):
    reader = PdfReader(path)
    return reader.get_num_pages()

def get_pdf_text_by_page(path):
    pages = extract_pages(path)
    
    text_by_page = []
    page_num = 1
    for page in pages:
        page_dir = {"page": page_num, "text": page.extract_text()}
        text_by_page.append(page_dir)
        page_num = page_num + 1
    
    return text_by_page
