import google.generativeai as genai
from openai import OpenAI
GEMINI_API_KEY = "AIzaSyASTEWW4sTDNWcuTcD2AWXmuQR1ELy7X8M"
genai.configure(api_key=GEMINI_API_KEY)
models = genai.list_models()
for m in models:
    print(m.name, "supports generate_content" if "generateContent" in m.supported_generation_methods else "")
