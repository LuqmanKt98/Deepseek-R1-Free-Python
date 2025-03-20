from openai import OpenAI
import os

# Your OpenRouter API key
API_KEY = "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"

def get_openai_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY
    )

def chat_with_bot(user_input):
    client = get_openai_client()
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "http://localhost",  # Required for OpenRouter
            "X-Title": "Python Chatbot",  # Required for OpenRouter
        },
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"ChatBot: {response}")
