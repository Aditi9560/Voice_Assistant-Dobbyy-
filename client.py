from openai import OpenAI

client = OpenAI(
    api_key="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",)


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
