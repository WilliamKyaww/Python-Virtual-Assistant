import openai

OPENAI_KEY = "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"
openai.api_key = OPENAI_KEY

def send_to_chatGPT(message, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    message.append(response.choices[0].message)
    return message

messages = [
    {
        "role": "user",
        "content": "You are Clockwork, a virtual AI personal assistant system created by William Kyaw through Python using the OpenAI api. Please speak like JARVIS in a calm and sophisticated British accent",
    }
]

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})
    response = send_to_chatGPT(messages)
    print("ChatGPT:", response)
