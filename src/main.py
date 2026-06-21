import json
from tools import search_tool
from tools.rag_tool import answer_question, answer_question_verbose
from tools.index_tool import build_index, save_index, load_index
from tools.embedding_tool import enrich_index

# index, _ = build_index("./tools/testFiles/")
# index = enrich_index(index)

index_path = "./tools/index.json"
# save_index(index_path, index)

for text in answer_question_verbose(index_path, "Power Delay Profile", "Como se calcula el Power delay profile?", top_k=10):
    print(text, end='', flush=True)
