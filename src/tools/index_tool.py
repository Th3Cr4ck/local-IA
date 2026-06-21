import json

from . import file_tool as ft
from .pdf_tool import read_pdf


def build_index(directory, recursive=True, start_id=0):

    def chunk_text(text, chunk_size=800, overlap=100):
        start = 0
        while (start < len(text)):
            end = start + chunk_size
            chunk = text[start:end]

            yield chunk

            start += chunk_size - overlap

    files = ft.list_contents(directory)
    index = []
    entry_id = start_id
    
    for file in files:

        if ft.file_is_dir(file) and recursive:
            subdir_index, entry_id = build_index(file, start_id=entry_id)
            index.extend(subdir_index)
            continue
        

        suffix = ft.get_suffix(file)
        if suffix == '.pdf':

            pdf_text = read_pdf(file)
            for chunk in chunk_text(pdf_text):
                index.append({
                    "id": entry_id,
                    "path": str(ft.get_abs_path(file)),
                    "file": str(ft.get_name(file)),
                    "text": chunk,
                })
                entry_id += 1

        elif suffix == '.txt' or suffix == '.md':

            file_text = ft.read_text_file(file)
            for chunk in chunk_text(file_text):
                index.append({
                    "id": entry_id,
                    "path": str(ft.get_abs_path(file)),
                    "file": str(ft.get_name(file)),
                    "text": chunk,
                })
                entry_id += 1

        #else: Unhandled type

    return index, entry_id

def save_index(path, index):
    with open(path, "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

def load_index(path):
    with open(path) as f:
        index = json.load(f)
    return index

