from openai import OpenAI
import os

def get_openai_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")  # Correct way to get the API key
    )

def chat_with_bot(user_input):
    client = get_openai_client()
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Change to your site URL
            "X-Title": "<YOUR_SITE_NAME>",  # Optional: Change to your site name
        },
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    # Set API key before running the script
    os.environ["OPENROUTER_API_KEY"] = "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"

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"ChatBot: {response}")
