import google.generativeai as genai
from openai import OpenAI
import ast
import re

GEMINI_API_KEY = "AIzaSyASTEWW4sTDNWcuTcD2AWXmuQR1ELy7X8M"
genai.configure(api_key=GEMINI_API_KEY)
def get_models(api_key):
    client=OpenAI(api_key="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",
            base_url="https://api.groq.com/openai/v1")
    models = client.models.list()
    model_list=[model.id for model in models]
    return model_list
def convert(response):
    # Your raw response from Gemini
    gemini_response = response
    # Step 1: Extract the lists from the response
    lists = re.findall(r"\[.*?\]", gemini_response)

    # Step 2: Convert the string lists to Python lists
    final_list = []
    combined=[]
    for l in lists:
        combined += ast.literal_eval(l)
    final_list = list(dict.fromkeys(combined))
    return final_list
def print_models(api_key):
    l=get_models(api_key)
    r=' '.join(l)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(f"Here is a list of AI model names: {r}. From this list, give me only the models that support generating content based on English text input. Also include any models that can accept both text and file inputs like images, audio, or documents. Ignore models meant only for embeddings, fine-tuning, classification, or encoding. Return the result as list: models that accept only text input, and that accept both text and files.\
        remember i dont want any other word except the model names in the output.")
    output = response.text.strip()
    opt=output.replace("**","")
    opt=opt.replace("*","")
    li=convert(opt)
    return li
