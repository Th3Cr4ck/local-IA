import json
from tools import search_tool
from tools.rag_tool import answer_question, answer_question_verbose
from tools.index_tool import build_index, save_index, load_index
from tools.embedding_tool import enrich_index

create_index = True
create_index = False

index_path = "./tools/index.json"

if create_index:
    index, _ = build_index("./tools/testFiles/")
    index = enrich_index(index)
    save_index(index_path, index)

for text in answer_question_verbose(index_path, 
                                    "Cuales son los dos modos de funcionamiento del algoritmo cordic?", 
                                    top_k=5):
    print(text, end='', flush=True)
