from openai import OpenAI
def get_response(prompt,api_key,model,platform):
    if platform=="OpenRouter":
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        )
        completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        )
        return completion.choices[0].message.content
    elif platform=="Groq":
        client=OpenAI(api_key=api_key,
                base_url="https://api.groq.com/openai/v1")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role":"system","content":"You are a helpful assistant."},
                    {"role":"user","content":prompt}]
        )
        return response.choices[0].message.content
