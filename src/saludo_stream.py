from ollama import chat

stream = chat(
    model='phi4-mini',
    messages=[{'role': 'user', 'content': 'What is 17 × 23?'}],
    stream=True,
)

print("Respuesta: ", end="", flush=True)
for chunk in stream:
    # Si el modelo soporta 'thinking' (como DeepSeek), se maneja aparte
    if hasattr(chunk.message, 'thinking') and chunk.message.thinking:
        # Opcional: mostrar el pensamiento entre corchetes
        print(f"[Pensando: {chunk.message.thinking}]", end="", flush=True)
    elif chunk.message.content:
        print(chunk.message.content, end="", flush=True)
print()  # salto de línea final
