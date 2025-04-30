import google.generativeai as genai
from openai import OpenAI
import ast
import re
import os

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
def get_models(api_key):
    client=OpenAI(api_key=api_key,
            base_url="https://api.groq.com/openai/v1")
    models = client.models.list()
    model_list=[model.id for model in models]
    return model_list
def convert(response):
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
def print_models_gq(api_key):
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
def print_models_op(api_key):
    by_family = {
    "Qwen": [
        "qwen/qwen3-30b-a3b:free", "qwen/qwen3-8b:free", "qwen/qwen3-14b:free",
        "qwen/qwen3-32b:free", "qwen/qwen3-235b-a22b:free",
        "qwen/qwen2.5-vl-3b-instruct:free", "qwen/qwen2.5-vl-32b-instruct:free",
        "qwen/qwen2.5-vl-72b-instruct:free", "qwen/qwen-2.5-coder-32b-instruct:free",
        "qwen/qwen-2.5-7b-instruct:free", "qwen/qwen-2.5-72b-instruct:free",
        "qwen/qwen-2.5-vl-7b-instruct:free", "qwen/qwq-32b:free",
        "qwen/qwq-32b-preview:free"
    ],
    "Meta LLaMA": [
        "meta-llama/llama-4-maverick:free", "meta-llama/llama-4-scout:free",
        "meta-llama/llama-3.3-70b-instruct:free", "meta-llama/llama-3.2-3b-instruct:free",
        "meta-llama/llama-3.2-1b-instruct:free", "meta-llama/llama-3.2-11b-vision-instruct:free",
        "meta-llama/llama-3.1-405b:free", "meta-llama/llama-3.1-8b-instruct:free"
    ],
    "DeepSeek": [
        "deepseek/deepseek-prover-v2:free", "deepseek/deepseek-v3-base:free",
        "deepseek/deepseek-chat-v3-0324:free",
        "deepseek/deepseek-chat:free", "deepseek/deepseek-r1:free",
        "deepseek/deepseek-r1-distill-qwen-32b:free", "deepseek/deepseek-r1-distill-qwen-14b:free",
        "deepseek/deepseek-r1-distill-llama-70b:free"
    ],
    "Mistral": [
        "mistralai/mistral-small-3.1-24b-instruct:free", "mistralai/mistral-small-24b-instruct-2501:free",
        "mistralai/mistral-7b-instruct:free", "mistralai/mistral-nemo:free"
    ],
    "Google": [
        "google/gemma-2-9b-it:free", "google/gemma-3-1b-it:free", "google/gemma-3-4b-it:free",
        "google/gemma-3-12b-it:free", "google/gemma-3-27b-it:free", "google/gemini-2.0-flash-exp:free",
        "google/learnlm-1.5-pro-experimental:free"
    ],
    "NVIDIA": [
        "nvidia/llama-3.3-nemotron-super-49b-v1:free", "nvidia/llama-3.1-nemotron-ultra-253b-v1:free"
    ],
    "THUDM (GLM)": [
        "thudm/glm-z1-9b:free", "thudm/glm-4-9b:free", "thudm/glm-z1-32b:free", "thudm/glm-4-32b:free"
    ],
    "Others": [
        "shisa-ai/shisa-v2-llama3.3-70b:free", "arliai/qwq-32b-arliai-rpr-v1:free",
        "agentica-org/deepcoder-14b-preview:free", "moonshotai/kimi-vl-a3b-thinking:free",
        "moonshotai/moonlight-16b-a3b-instruct:free", "rekaai/reka-flash-3:free",
        "tngtech/deepseek-r1t-chimera:free", "open-r1/olympiccoder-32b:free",
        "cognitivecomputations/dolphin3.0-r1-mistral-24b:free", "cognitivecomputations/dolphin3.0-mistral-24b:free",
        "allenai/molmo-7b-d:free", "featherless/qwerky-72b:free", "huggingfaceh4/zephyr-7b-beta:free"
    ]
}
    return by_family
