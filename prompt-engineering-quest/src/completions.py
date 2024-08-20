import openai

def get_openai_completion(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content']
