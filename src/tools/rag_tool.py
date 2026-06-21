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
    prompt += " Te recuerdo que solo uses la informacion que te paso como contexto. Si no tienes suficiente contexto dilo y no respondas la pregunta"
    return prompt

def answer_question(index_path, look_for, query=""):

    chunks = retrieve(look_for, index_path)

    prompt = build_prompt(chunks, query, look_for)
    print(prompt)

    stream = generate(
        model='llama3.1-gpu',
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        yield chunk['response']

def answer_question_verbose(index_path, look_for, query="", top_k=5):
    chunks = retrieve(look_for, index_path, top_k)

    prompt = build_prompt(chunks, query, look_for)
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

