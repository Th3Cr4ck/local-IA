from index_tool import load_index
from pdf_tool import get_pdf_text_by_page
import file_tool as ft


def search_text(query, index_path, file=None):
    
    results = []

    index = load_index(index_path)
    for entry in index:

        if file is not None:
            if entry["file"] != file:
                continue

        if query.lower() in entry["text"].lower():
                results.append(entry)
        
    return results

def search_pdf(query, pdf):
    results = []

    pages = get_pdf_text_by_page(pdf)

    for page in pages:
        if query.lower() in page["text"].lower():
            results.append(page)
    
    return results

def search_file(query, file):
    results = []

    lines = ft.get_text_by_line(file)

    for line in lines:
        if query.lower() in line["text"].lower():
            results.append(line)

    return results

def search_directory(query,  directory):
    dir_contents = ft.list_contents(directory)

    results = []

    for file in dir_contents:
        if ft.get_suffix(file) == '.pdf':
            results.extend(search_pdf(query, file))
        elif not ft.file_is_dir(file):
            results.extend(search_file(query, file))
        # else:  File is directory

    return results


def retrieve(query, index_path, top_k=5):
    return search_text(query, index_path)[:top_k]

