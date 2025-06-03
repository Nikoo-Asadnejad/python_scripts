import openai

openai.api_key = "api_key"

def correct_grammar(text):
    prompt = f"Correct this sentence's grammar and punctuation:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

text = input("Enter a sentence to check: ")
print("Corrected:", correct_grammar(text))
