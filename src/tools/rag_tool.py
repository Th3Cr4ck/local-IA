from .search_tool import retrieve
from ollama import generate

def build_prompt(context, query):
    prompt = ""

    if query == '':
        return 'Indicame que mi query esta vacio.'
    else:
        prompt = f"""Contexto: {context}
        Responde solo con la informacion del contexto que te acabo de dar, nada mas.
        {query}
        Si el contexto contiene información suficiente, responde de manera directa. Puedes utilizar sinónimos y relacionar conceptos equivalentes siempre que la relación esté explícitamente sustentada en el contexto.
        Si realmente no existe información relevante en el contexto, responde unicamente:
        'No tengo suficiente contexto para responder la pregunta.'
        """
    return prompt

def answer_question(index_path, query):

    chunks = retrieve(query, index_path)

    prompt = build_prompt(chunks, query)
    print(prompt)

    stream = generate(
        model='llama3.1-gpu',
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        yield chunk['response']

def answer_question_verbose(index_path, query, top_k=5):
    chunks = retrieve(query, index_path, top_k)

    prompt = build_prompt(chunks, query)
    print(prompt)

    stream = generate(
        model='llama3.1-gpu',
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        if chunk.get("done", False):

            prompt_tps = (
                chunk["prompt_eval_count"]
                / (chunk["prompt_eval_duration"] / 1e9)
            )

            gen_tps = (
                chunk["eval_count"]
                / (chunk["eval_duration"] / 1e9)
            )

            print("\n=== Rendimiento ===")
            print(f"Prompt TPS: {prompt_tps:.2f}")
            print(f"Generación TPS: {gen_tps:.2f}")
            print("Prompt tokens:", chunk["prompt_eval_count"])

        yield chunk["response"]

