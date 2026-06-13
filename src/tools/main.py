import file_tool as ft
import index_tool as it
import search_tool as st


if ft.file_exists("index.json"):
    ft.remove("index.json")

if ft.file_exists("search_results.txt"):
    ft.remove("search_results.txt")

index, _ = it.build_index('./testFiles/')
it.save_index("index.json", index)

search = st.search_text('linea', 'index.json')
str_search = '\n'.join(str(dic) for dic in search)

ft.write_text_file('search_results.txt', str_search)
