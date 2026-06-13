import json
from tools.rag_tool import answer_question
from tools.index_tool import build_index, save_index

index, _ = build_index("./tools/testFiles/")
index_path = "./tools/index.json"
save_index(index_path, index)

for text in answer_question(index_path, "OFDM", "Resume y explica que es OFDM"):
    print(text, end='', flush=True)
