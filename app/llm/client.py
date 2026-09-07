import ollama

MODEL_NAME = "llama3.2"

def ask_llm(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return response['message']['content']

"""Communicates with the LLM."""