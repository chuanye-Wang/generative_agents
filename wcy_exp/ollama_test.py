import ollama
MODEL = ''
def ChatGPT_request(prompt):
    """
    Given a prompt, make a request to the Ollama server and return the response.
    ARGS:
        prompt: a str prompt
    """
    completion = ollama.chat(
      model=MODEL,
      messages=[{"role": "user", "content": prompt}],
    )
    return completion['message']['content']

if __name__ == "__main__":
    # Example usage
    while True:
        user_input = input("🧑‍🔬:")
        if user_input.lower() == 'exit' or user_input.lower() == 'e':
            break
        response = ChatGPT_request(user_input)
        print("🤖：", response)