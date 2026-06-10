from pathlib import Path
import shutil

# Reading directories
def list_contents(path='.'):
    p = Path(path)
    return list(p.iterdir())

def list_subdir(path):
    p = Path(path)
    return [f for f in p.iterdir() if f.is_dir()]

def find_files(pattern, path='.'):
    p = Path(path)
    return list(p.glob(pattern))

def file_exists(path):
    return Path(path).exists()

def file_is_dir(path):
    return Path(path).is_dir()

def get_metadata(path):
    p = Path(path)
    return p.stat()

def get_suffix(path):
    p = Path(path)
    return p.suffix

def get_name(path):
    p = Path(path)
    return p.name

def get_abs_path(path):
    p = Path(path)
    return p.absolute()

# Reading and writing files
def read_text_file(path):
    p = Path(path)
    return p.read_text()

def get_text_by_line(path):
    data = []

    with open(path) as f:
        for lineno, line in enumerate(f, start=1):
            data.append({
                "lineno": lineno,
                "text": line.rstrip()
            })

    return data

def write_text_file(path, text):
    p = Path(path)
    return p.write_text(text)

# Copying and moving
def copy(src, dst):
    shutil.copy2(src, dst)

def copytree(src, dst):
    shutil.copytree(src, dst)

def move(src, dst):
    """
    Recursively move a file or directory (src) to another location and return the destination.
    """
    shutil.move(src, dst)

