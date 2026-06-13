import json
import file_tool as ft
from pdf_tool import get_pdf_text_by_page


def build_index(directory, recursive=True, start_id=0):

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

            pages = get_pdf_text_by_page(file)
            for page in pages:
                index.append({
                    "id": entry_id,
                    "path": str(ft.get_abs_path(file)),
                    "file": ft.get_name(file),
                    "page": page["page"],
                    "text": page["text"]
                })
                entry_id += 1

        elif suffix == '.txt' or suffix == '.md' or suffix == '.json':

            lines = ft.get_text_by_line(file)
            for line in lines:
                index.append({
                    "id": entry_id,
                    "path": str(ft.get_abs_path(file)),
                    "file": ft.get_name(file),
                    "line": line["lineno"],
                    "text": line["text"]
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

