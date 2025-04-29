from openai import OpenAI
print(dir(OpenAI))
client=OpenAI(api_key="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",
              base_url="https://api.groq.com/openai/v1")
models = client.models.list()
for model in models:
    print(model.id)
def get_response(prompt,api_key,model="llama2-70b-chat"):
    client=OpenAI(api_key=api_key,
            base_url="https://api.groq.com/openai/v1")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role":"system","content":"You are a helpful assistant."},
                {"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
