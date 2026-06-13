from .search_tool import retrieve
from ollama import generate

def build_prompt(context, query='', look_for=''):
    prompt = ""

    if query == '' and look_for == '':
        return ''

    if query == '':
        prompt = f"""Contexto: {context}
        Responde solo con la informacion del contexto que te acabo de dar, nada mas,
        dame toda la informacion que hayas podido recopilar de: {look_for}
        """
    else:
        prompt = f"""Contexto: {context}
        Responde solo con la informacion del contexto que te acabo de dar, nada mas.
        {query}
        """
    prompt += "Si no tienes suficiente contexto dilo y no respondas la pregunta"
    return prompt

def answer_question(index_path, look_for, query=""):

    chunks = retrieve(look_for, index_path)

    prompt = build_prompt(chunks, query, look_for)
    print(prompt)

    stream = generate(
        model='phi4-mini-gpu',
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        yield chunk['response']


