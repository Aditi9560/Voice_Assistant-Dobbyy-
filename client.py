from openai import OpenAI

client = OpenAI(
    api_key="openaikey"

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant dobby."},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)

print(completion.choices[0].message.content)
